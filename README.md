# Commit Critters 🌱🏆

> An openly declared GitHub achievement farm, with a tiny terminal creature to keep us company.

Yes, this repo is for farming the easy GitHub achievements. We're documenting the recipes, trying them on our own project, and recording what actually happens. The crop is badges. The farmhand is a goblin. The farming equipment is Git.

The small, runnable project is **Commit Critters**: a creature that reacts to your local repository. Commits help it grow, unfinished changes give it something to compost, and a quiet week sends it to sleep.

## Visit the farm

Requires Python 3.10+ and Git. No dependencies or API token needed to run the critter.

```sh
git clone https://github.com/Zachary260325/commit-critters.git
cd commit-critters
python3 critters.py --demo
python3 critters.py
python3 critters.py --quests
```

On Windows, use `py -3` in place of `python3`.

```text
       /\_/\
      ( o.o )
       > ^ <     Nibble, the badge goblin

Mood: composting
Level: 4 | Local commits: 7 | Changes: 3
Branch: sprout/new-feature

3 unfinished changes. Excellent compost.
```

Inspect another repository with `python3 critters.py --repo /path/to/repo`.

Local commits feed the creature; **they are not a GitHub achievement counter**. The program reads Git metadata and never creates commits, issues, pull requests, or stars.

## What we're farming

| Achievement | Commonly observed unlock | Our plan |
| --- | --- | --- |
| YOLO | Merge your own pull request without code review | Ship a small feature through a PR; run the checks, then self-merge |
| Pair Extraordinaire | Have a co-authored pull request merged | Credit the assistant's actual work and test whether GitHub recognizes that identity |
| Pull Shark | Have 2 pull requests merged; bronze at 16 | Let real feature and documentation PRs accumulate |
| Quickdraw | Close an issue or PR within 5 minutes of opening it | Document a short, completed maintenance task and close it promptly |

**[Read the recipes →](docs/ACHIEVEMENTS.md)** for steps, co-author formatting, higher tiers, and verification tips.

GitHub controls the awards. The unlock rules above come from [community observations](https://github.com/Schweinepriester/github-profile-achievements), rather than a published guarantee. **AI co-author credit is possible; its eligibility for Pair Extraordinaire is an unverified experiment here.**

Stars, sponsorships, and accepted Discussion answers are outside this farm's current scope. We are leaving retired and experimental badges alone too.

## Field notes

At the start, [Zachary260325](https://github.com/Zachary260325?tab=achievements) publicly displayed **Pull Shark bronze (×2)** and **Quickdraw**, checked on October 16, 2026. Our first new target is YOLO. Pair Extraordinaire is a separate experiment, not a promised reward.

The [first feature PR](https://github.com/Zachary260325/commit-critters/pull/1) passed GitHub Actions and was self-merged with Codex credit. Neither target badge was visible at our first check immediately afterward. The [experiment log](docs/EXPERIMENTS.md) records the evidence and separates completed actions from badges visibly awarded. The [contribution guide](CONTRIBUTING.md) explains how new features become PRs.

## Work on the critter

```sh
python3 -m unittest discover -s tests -v
```

Small features welcome: new creature personalities, better terminal output, and useful Git summaries. Keep farming activity in this repository and credit the contributors who actually helped.

MIT licensed. Farm responsibly. Pet the goblin.
