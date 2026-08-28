#!/usr/bin/env python3
"""Deterministic repository validation for Project Definition Skills.

Uses Python's standard library only so contributors and CI do not need to
install project-specific dependencies.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
INLINE_SKILL_PATH_RE = re.compile(r"`((?:references|assets|scripts)/[^`\s]*)`")

REQUIRED_ROOT_FILES = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CHANGELOG.md",
)

REQUIRED_EVAL_HEADINGS = (
    "Purpose",
    "Input",
    "Environment",
    "Expected behavior",
    "Forbidden behavior",
    "Critical requirements",
    "Scoring focus",
)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks = 0

    def check(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.errors.append(message)

    def warn(self, condition: bool, message: str) -> None:
        self.checks += 1
        if not condition:
            self.warnings.append(message)


def read_text(path: Path, report: Report) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.errors.append(f"Cannot read {path}: {exc}")
        return None


def parse_frontmatter(text: str, path: Path, report: Report) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        report.errors.append(f"{path}: SKILL.md must start with YAML frontmatter ('---').")
        return None

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        report.errors.append(f"{path}: YAML frontmatter is not closed with '---'.")
        return None

    data: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            report.errors.append(f"{path}:{line_number}: unsupported frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
            value = value[1:-1]
        data[key] = value
    return data


def validate_root(root: Path, report: Report) -> None:
    for relative in REQUIRED_ROOT_FILES:
        report.check((root / relative).is_file(), f"Missing required root file: {relative}")


def validate_skills(root: Path, report: Report) -> None:
    skills_root = root / "skills"
    report.check(skills_root.is_dir(), "Missing skills/ directory.")
    if not skills_root.is_dir():
        return

    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
    report.check(bool(skill_dirs), "No skill directories found under skills/.")

    for skill_dir in skill_dirs:
        report.check(
            bool(SKILL_NAME_RE.fullmatch(skill_dir.name)),
            f"Invalid skill directory name '{skill_dir.name}'; expected lowercase kebab-case.",
        )

        skill_file = skill_dir / "SKILL.md"
        report.check(skill_file.is_file(), f"{skill_dir}: missing required SKILL.md.")
        if not skill_file.is_file():
            continue

        text = read_text(skill_file, report)
        if text is None:
            continue

        frontmatter = parse_frontmatter(text, skill_file.relative_to(root), report)
        if frontmatter is not None:
            name = frontmatter.get("name", "").strip()
            description = frontmatter.get("description", "").strip()
            report.check(bool(name), f"{skill_file.relative_to(root)}: frontmatter requires 'name'.")
            report.check(bool(description), f"{skill_file.relative_to(root)}: frontmatter requires 'description'.")
            if name:
                report.check(
                    name == skill_dir.name,
                    f"{skill_file.relative_to(root)}: frontmatter name '{name}' must match folder '{skill_dir.name}'.",
                )
                report.check(
                    bool(SKILL_NAME_RE.fullmatch(name)),
                    f"{skill_file.relative_to(root)}: skill name must be lowercase kebab-case.",
                )
                report.check(len(name) <= 64, f"{skill_file.relative_to(root)}: skill name exceeds 64 characters.")
            if description:
                report.check(
                    len(description) <= 1024,
                    f"{skill_file.relative_to(root)}: description exceeds 1024 characters.",
                )

        line_count = len(text.splitlines())
        report.warn(
            line_count <= 500,
            f"{skill_file.relative_to(root)} has {line_count} lines; keep SKILL.md lean and prefer referenced resources.",
        )

        for match in INLINE_SKILL_PATH_RE.finditer(text):
            raw_target = match.group(1).rstrip(".,;:)")
            target = skill_dir / raw_target
            report.check(
                target.exists(),
                f"{skill_file.relative_to(root)} references missing skill resource: {raw_target}",
            )


def markdown_target_to_path(source: Path, target: str, root: Path) -> Path | None:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()

    lowered = target.lower()
    if not target or target.startswith("#") or lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return None

    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None

    target = unquote(target)
    if target.startswith("/"):
        return root / target.lstrip("/")
    return source.parent / target


def validate_markdown_links(root: Path, report: Report) -> None:
    ignored_parts = {".git", ".venv", "venv", "node_modules"}
    for path in sorted(root.rglob("*.md")):
        if any(part in ignored_parts for part in path.parts):
            continue
        text = read_text(path, report)
        if text is None:
            continue
        for match in MARKDOWN_LINK_RE.finditer(text):
            raw_target = match.group(1)
            resolved = markdown_target_to_path(path, raw_target, root)
            if resolved is None:
                continue
            report.check(
                resolved.exists(),
                f"Broken relative Markdown link in {path.relative_to(root)}: {raw_target}",
            )


def section_body(text: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else None


def validate_evals(root: Path, report: Report) -> None:
    eval_root = root / "evals" / "project-definition"
    if not eval_root.exists():
        report.warnings.append("No project-definition eval suite found; behavioral regression coverage is absent.")
        return

    for required in ("README.md", "rubric.md", "case-template.md"):
        report.check((eval_root / required).is_file(), f"Missing eval support file: evals/project-definition/{required}")

    cases_dir = eval_root / "cases"
    report.check(cases_dir.is_dir(), "Missing evals/project-definition/cases/ directory.")
    if not cases_dir.is_dir():
        return

    cases = sorted(cases_dir.glob("*.md"))
    report.check(bool(cases), "No evaluation case files found.")

    case_name_re = re.compile(r"^\d{3}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
    for case in cases:
        relative = case.relative_to(root)
        report.check(bool(case_name_re.fullmatch(case.name)), f"Invalid eval case filename: {relative}")
        text = read_text(case, report)
        if text is None:
            continue

        report.check(text.lstrip().startswith("# Case "), f"{relative}: first heading must identify the case.")
        for heading in REQUIRED_EVAL_HEADINGS:
            body = section_body(text, heading)
            report.check(body is not None, f"{relative}: missing '## {heading}' section.")
            if body is not None:
                report.check(bool(body.strip()), f"{relative}: '## {heading}' section must not be empty.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Agent Skills repository structure and internal consistency.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Repository root")
    args = parser.parse_args()

    root = args.root.resolve()
    report = Report()

    validate_root(root, report)
    validate_skills(root, report)
    validate_markdown_links(root, report)
    validate_evals(root, report)

    if report.warnings:
        print("Warnings:")
        for warning in report.warnings:
            print(f"  - {warning}")
        print()

    if report.errors:
        print("Validation failed:")
        for error in report.errors:
            print(f"  - {error}")
        print(f"\n{len(report.errors)} error(s), {len(report.warnings)} warning(s), {report.checks} checks.")
        return 1

    print(f"Validation passed: {report.checks} checks, {len(report.warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
