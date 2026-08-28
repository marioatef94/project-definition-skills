#!/usr/bin/env python3
"""Install a repository skill into a user-selected Agent Skills directory."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy a skill from this repository into an Agent Skills-compatible target directory. "
            "The target path is supplied by the user because skill discovery locations vary by client."
        )
    )
    parser.add_argument(
        "--skill",
        default="project-definition",
        help="Skill directory name under ./skills (default: project-definition).",
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Directory that should contain installed skill folders.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed skill directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    source = repo_root / "skills" / args.skill
    target_root = Path(args.target).expanduser().resolve()
    destination = target_root / args.skill

    if not source.is_dir() or not (source / "SKILL.md").is_file():
        print(f"error: skill '{args.skill}' was not found at {source}", file=sys.stderr)
        return 2

    target_root.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        if not args.force:
            print(
                f"error: {destination} already exists; re-run with --force to replace it",
                file=sys.stderr,
            )
            return 3
        if destination.is_dir():
            shutil.rmtree(destination)
        else:
            destination.unlink()

    shutil.copytree(source, destination)

    installed_manifest = destination / "SKILL.md"
    if not installed_manifest.is_file():
        print("error: installation finished without SKILL.md", file=sys.stderr)
        return 4

    print(f"Installed '{args.skill}' to {destination}")
    print("Configure your AI client to discover skills from the target directory if needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
