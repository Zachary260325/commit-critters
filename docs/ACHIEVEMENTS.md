# The achievement recipes

This repo openly farms easy GitHub achievements while building a small terminal toy. These recipes describe widely observed triggers; GitHub decides eligibility and award timing. A completed action and a visibly awarded badge are separate results.

## YOLO: ship the tiny thing

**Observed trigger:** merge your own pull request without code review.

1. Create a branch in your own repository.
2. Make a small change, such as adding the critter or improving its quest board.
3. Commit and push the branch, then open a pull request into the default branch.
4. Run the project's checks. Self-merge the PR without a formal code review.
5. Visit your profile's Achievements section. Add the PR URL and the observed outcome to [the log](EXPERIMENTS.md).

CI passing is compatible with this experiment: automated tests are different from a code review. Use a personal project whose rules allow self-merging; leave another project's review requirements in place.

## Pair Extraordinaire: bring a co-author

**Observed trigger:** a merged pull request containing a co-authored commit. Commonly reported tiers are **1, 10, 24, and 48** co-authored merged PRs.

1. Make a contribution together.
2. Ask the contributor which GitHub-associated email they want credited. Their GitHub no-reply address works when correctly associated with the account.
3. Put a blank line between the commit message body and the co-author trailer:

```text
Add a new creature personality

Co-authored-by: Contributor Name <their-github-linked-email>
```

The name and address above are placeholders. Replace them with the actual contributor's details.

4. Open and merge a PR containing the commit. If squash-merging, keep the trailer in the resulting commit message.
5. Check the commit's co-author display and your profile's Achievements section separately.

### Can the co-author be AI?

AI attribution is supported: [VS Code documents AI co-author trailers](https://code.visualstudio.com/updates/v1_110#_ai-co-author-attribution-for-commits). That does **not** establish badge eligibility for every assistant identity. [GitHub requires an account-associated email for contribution attribution](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors).

We credit Codex when it contributes, and will record whether GitHub recognizes that attribution and awards Pair Extraordinaire. Until that is observed, the AI route stays **unverified**. Adding a trailer is an experiment, not a guaranteed unlock.

## Pull Shark: use the PR workflow

**Observed trigger:** have **2** of your pull requests merged. Higher tiers are commonly reported at **16 / 128 / 1,024**.

1. Put a useful change on a branch and open a PR.
2. Merge it after the appropriate checks.
3. Repeat for another useful change.
4. Check your profile and record the visible result.

Your own repository can be used for the experiment. Creating commits directly on the default branch is not the same as having PRs merged. Local commit totals from `critters.py` therefore cannot tell you your badge progress.

Zachary260325 already displayed bronze at the start of this project. Silver is a longer-term target, not a reason to manufacture 112 tiny PRs.

## Quickdraw: finish a small task promptly

**Observed trigger:** close an issue or PR within **5 minutes** of opening it.

1. Choose a task you can complete quickly in your own repository, such as verifying the documented demo command.
2. Open an issue describing the check.
3. Run the check and note the result.
4. Close the issue within five minutes of its opening time.
5. Check your profile and record what appears.

Zachary260325 already displayed this badge at the start. Other visitors can use the recipe in their own repositories.

## Leave these crops for later

| Achievement | Reason it is outside the current plan |
| --- | --- |
| Starstruck | Needs other people to star a repository |
| Galaxy Brain | Needs accepted answers in GitHub Discussions |
| Public Sponsor | Requires sponsorship spending |
| Arctic Code Vault Contributor / Mars 2020 Contributor | Historical awards with closed eligibility windows |
| Heart On Your Sleeve / Open Sourcerer | Experimental or disabled according to the community reference |

## Check the harvest

Open [your profile](https://github.com/settings/profile) and check whether achievement display is enabled, then inspect the Achievements section of your public profile. GitHub's [profile reference](https://docs.github.com/en/account-and-profile/reference/profile-reference#earning-achievements) explains the achievement details and contributing-event links.

If an award does not appear, record **action completed; badge not observed**. Check that the intended account authored the PR, the PR was actually merged, and any co-author trailer survived the merge. There is no guaranteed processing deadline here, and the farm does not repeatedly create events to force an award.

## Sources

- [GitHub Docs: earning achievements](https://docs.github.com/en/account-and-profile/reference/profile-reference#earning-achievements) — official description of the feature, currently in public preview.
- [GitHub Docs: commits with multiple authors](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors) — official trailer format and email association requirements.
- [VS Code: AI co-author attribution](https://code.visualstudio.com/updates/v1_110#_ai-co-author-attribution-for-commits) — official support for AI attribution, not a badge eligibility guarantee.
- [Community achievement reference](https://github.com/Schweinepriester/github-profile-achievements) — observed unlock triggers, tiers, and retired/disabled statuses.

Sources checked October 16, 2026. These guides may change as GitHub changes its behavior.
