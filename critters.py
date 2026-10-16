#!/usr/bin/env python3
"""A tiny, read-only terminal critter powered by local Git activity."""

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import subprocess
import sys


@dataclass(frozen=True)
class Garden:
    branch: str
    commits: int
    recent: int
    changes: int


def git(repo: Path, *args: str, allowed: tuple[int, ...] = (0,)) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except FileNotFoundError as error:
        raise ValueError("Git is missing. Install Git or try --demo.") from error
    if result.returncode not in allowed:
        raise ValueError("Cannot read that Git repository. Try --demo for a preview.")
    return result.stdout


def change_count(porcelain: str) -> int:
    """Count porcelain v1 -z entries, including two-path renames only once."""
    entries = iter(porcelain.split("\0"))
    count = 0
    for entry in entries:
        if not entry:
            continue
        count += 1
        if "R" in entry[:2] or "C" in entry[:2]:
            next(entries, None)
    return count


def inspect(repo: Path) -> Garden:
    git(repo, "rev-parse", "--show-toplevel")
    branch = git(repo, "symbolic-ref", "--short", "-q", "HEAD", allowed=(0, 1)).strip()
    head = git(repo, "rev-parse", "--verify", "--quiet", "HEAD", allowed=(0, 1)).strip()
    commits = int(git(repo, "rev-list", "--count", "HEAD")) if head else 0
    recent = int(git(repo, "rev-list", "--count", "--since=7.days.ago", "HEAD")) if head else 0
    status = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    return Garden(branch or "detached HEAD", commits, recent, change_count(status))


def render(garden: Garden) -> str:
    if garden.changes:
        mood = "composting"
        eyes = "o.o"
        noun = "change" if garden.changes == 1 else "changes"
        message = f"{garden.changes} unfinished {noun}. Excellent compost."
    elif garden.recent:
        mood = "celebrating"
        eyes = "^.^"
        message = "Fresh commits! The badge harvest smells promising."
    else:
        mood = "napping"
        eyes = "-.-"
        message = "A quiet garden. Nibble is dreaming of pull requests."
    level = (garden.commits + 1).bit_length()
    return "\n".join(
        [
            "       /\\_/\\",
            f"      ( {eyes} )",
            "       > ^ <     Nibble, the badge goblin",
            "",
            f"Mood: {mood}",
            f"Level: {level} | Local commits: {garden.commits} | Changes: {garden.changes}",
            f"Branch: {garden.branch}",
            "",
            message,
            "",
            "Local commits feed the critter; GitHub awards badges separately.",
        ]
    )


def quest_board() -> str:
    path = Path(__file__).with_name("quests.json")
    quests = json.loads(path.read_text(encoding="utf-8"))
    lines = ["THE ACHIEVEMENT FARM", "Community-observed recipes; GitHub decides the awards."]
    for quest in quests:
        lines.extend(["", f"{quest['name']} [{quest['status']}]", f"  Unlock: {quest['unlock']}"])
        for index, step in enumerate(quest["steps"], start=1):
            lines.append(f"  {index}. {step}")
        lines.append(f"  Note: {quest['note']}")
    lines.extend(["", "Full recipes and sources: docs/ACHIEVEMENTS.md"])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Git repository to inspect")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--demo", action="store_true", help="Preview a creature without reading Git")
    mode.add_argument("--quests", action="store_true", help="Show the achievement recipes")
    args = parser.parse_args(argv)
    try:
        if args.quests:
            print(quest_board())
        else:
            garden = Garden("sprout/new-feature", 7, 2, 3) if args.demo else inspect(args.repo)
            print(render(garden))
    except (ValueError, OSError) as error:
        print(f"Commit Critters: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
