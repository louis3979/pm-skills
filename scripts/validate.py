#!/usr/bin/env python3
"""
pm-skills marketplace validator.

Checks, with zero third-party dependencies:
- every .claude-plugin/plugin.json and the root marketplace.json are valid JSON
  with required fields (name, version, description) and name == directory name
- marketplace.json lists exactly the plugin directories present on disk
- every version (marketplace.json + every plugin.json) matches the newest
  CHANGELOG.md heading
- every skill has a SKILL.md with frontmatter name/description, and
  frontmatter name == directory name
- every command has frontmatter description + argument-hint
- README.md's headline counts and per-plugin "(N skills, M commands)" summaries
  match what's actually on disk

Exit code 0 = all checks passed. Exit code 1 = at least one error.
Run from the repo root: python3 scripts/validate.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"

errors: list[str] = []
warnings: list[str] = []


def error(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    result = {}
    for line in block.splitlines():
        line = line.strip()
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip().strip('"').strip("'")
            result[key] = val
    return result


def plugin_dirs() -> list[Path]:
    return sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and (p / ".claude-plugin" / "plugin.json").is_file()
    )


def skill_count(plugin: Path) -> int:
    skills = plugin / "skills"
    return sum(1 for s in skills.iterdir() if s.is_dir()) if skills.is_dir() else 0


def command_count(plugin: Path) -> int:
    cmds = plugin / "commands"
    return len(list(cmds.glob("*.md"))) if cmds.is_dir() else 0


def check_json_manifests() -> dict:
    """Returns {plugin_dir_name: version} for every valid plugin.json."""
    versions = {}

    if not MARKETPLACE.is_file():
        error("Missing .claude-plugin/marketplace.json")
        return versions
    try:
        mp = json.loads(MARKETPLACE.read_text())
    except json.JSONDecodeError as e:
        error(f"marketplace.json is invalid JSON: {e}")
        return versions

    for field in ("name", "version", "description"):
        if not mp.get(field):
            error(f"marketplace.json missing required field: {field}")

    listed = {p["name"] for p in mp.get("plugins", [])}
    on_disk = {p.name for p in plugin_dirs()}
    if listed != on_disk:
        only_listed = listed - on_disk
        only_disk = on_disk - listed
        if only_listed:
            error(f"marketplace.json lists plugins not on disk: {sorted(only_listed)}")
        if only_disk:
            error(f"plugins on disk not listed in marketplace.json: {sorted(only_disk)}")

    for p in mp.get("plugins", []):
        expected_source = f"./{p['name']}"
        if p.get("source") != expected_source:
            error(f"marketplace.json plugin '{p['name']}' has source '{p.get('source')}', expected '{expected_source}'")

    versions["__marketplace__"] = mp.get("version")

    for pdir in plugin_dirs():
        pj = pdir / ".claude-plugin" / "plugin.json"
        try:
            data = json.loads(pj.read_text())
        except json.JSONDecodeError as e:
            error(f"{pj.relative_to(ROOT)} is invalid JSON: {e}")
            continue
        for field in ("name", "version", "description"):
            if not data.get(field):
                error(f"{pj.relative_to(ROOT)} missing required field: {field}")
        if data.get("name") != pdir.name:
            error(f"{pj.relative_to(ROOT)} name '{data.get('name')}' != directory '{pdir.name}'")
        versions[pdir.name] = data.get("version")

    return versions


def check_versions_match_changelog(versions: dict) -> None:
    if not CHANGELOG.is_file():
        warn("No CHANGELOG.md found — version history is untracked")
        return
    text = CHANGELOG.read_text()
    m = re.search(r"^## v(\d+\.\d+\.\d+)", text, re.M)
    if not m:
        error("CHANGELOG.md has no '## vX.Y.Z' heading")
        return
    latest = m.group(1)
    for name, v in versions.items():
        if v != latest:
            error(f"{name} version '{v}' != CHANGELOG's latest 'v{latest}'")


def check_skills_and_commands() -> None:
    for pdir in plugin_dirs():
        skills_dir = pdir / "skills"
        if skills_dir.is_dir():
            for sdir in skills_dir.iterdir():
                if not sdir.is_dir():
                    continue
                skill_md = sdir / "SKILL.md"
                if not skill_md.is_file():
                    error(f"{sdir.relative_to(ROOT)} has no SKILL.md")
                    continue
                fm = parse_frontmatter(skill_md.read_text())
                if not fm.get("name"):
                    error(f"{skill_md.relative_to(ROOT)} missing frontmatter 'name'")
                elif fm["name"] != sdir.name:
                    error(f"{skill_md.relative_to(ROOT)} name '{fm['name']}' != directory '{sdir.name}'")
                if not fm.get("description"):
                    error(f"{skill_md.relative_to(ROOT)} missing frontmatter 'description'")

        cmds_dir = pdir / "commands"
        if cmds_dir.is_dir():
            for cfile in cmds_dir.glob("*.md"):
                fm = parse_frontmatter(cfile.read_text())
                if not fm.get("description"):
                    error(f"{cfile.relative_to(ROOT)} missing frontmatter 'description'")
                if not fm.get("argument-hint"):
                    warn(f"{cfile.relative_to(ROOT)} missing frontmatter 'argument-hint'")


def check_readme_counts() -> None:
    if not README.is_file():
        error("Missing README.md")
        return
    text = README.read_text()

    total_skills = sum(skill_count(p) for p in plugin_dirs())
    total_cmds = sum(command_count(p) for p in plugin_dirs())
    total_plugins = len(plugin_dirs())

    m = re.search(r"(\d+) skills and (\d+) chained workflows across (\d+) plugins", text)
    if not m:
        error("README.md headline 'N skills and M chained workflows across P plugins' not found")
    else:
        found = tuple(int(x) for x in m.groups())
        expected = (total_skills, total_cmds, total_plugins)
        if found != expected:
            error(f"README.md headline counts {found} != actual {expected}")

    for pdir in plugin_dirs():
        pattern = rf"<strong>\d+\.\s*{re.escape(pdir.name)}</strong>.*?\((\d+) skills?, (\d+) commands?\)"
        pm = re.search(pattern, text)
        if not pm:
            error(f"README.md has no '(N skills, M commands)' summary line for {pdir.name}")
            continue
        found = (int(pm.group(1)), int(pm.group(2)))
        expected = (skill_count(pdir), command_count(pdir))
        if found != expected:
            error(f"README.md counts for {pdir.name} {found} != actual {expected}")


def main() -> int:
    versions = check_json_manifests()
    check_versions_match_changelog(versions)
    check_skills_and_commands()
    check_readme_counts()

    total_skills = sum(skill_count(p) for p in plugin_dirs())
    total_cmds = sum(command_count(p) for p in plugin_dirs())
    print(f"Plugins: {len(plugin_dirs())} | Skills: {total_skills} | Commands: {total_cmds}\n")

    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}")

    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s). FAILED.")
        return 1
    print(f"All checks passed ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
