# Help on the farm

This is an achievement farm with a real terminal toy attached. Small contributions are welcome: creature messages, Git summaries, terminal compatibility, clearer recipes, and documented observations.

## Ship a change

1. Create a branch for one useful change.
2. Run `python3 critters.py --demo` and `python3 critters.py --quests`.
3. Run `python3 -m unittest discover -s tests -v`.
4. Open a PR explaining the behavior and how you checked it.
5. Credit actual contributors with a `Co-authored-by` trailer where appropriate.

The maintainer can self-merge small personal-project PRs for the YOLO experiment after checks pass. New PRs should improve the toy or its documentation; there is no automatic loop that creates PRs just to inflate a counter.

## Record observations

For badge experiments, include the merged PR URL, the co-author attribution when relevant, and what the profile actually displayed. A merged PR is evidence of a merge; it does not by itself prove an achievement was awarded.

See [the recipes](docs/ACHIEVEMENTS.md) and [field notes](docs/EXPERIMENTS.md). Keep any badge experiments in repositories you own or where the maintainer explicitly welcomes them.
