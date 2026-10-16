import contextlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import critters


class GitGardenTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.git("init", "--initial-branch=main")
        self.git("config", "user.name", "Critter Test")
        self.git("config", "user.email", "critter@example.invalid")

    def git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.repo), "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false", *args],
            check=True,
            capture_output=True,
            text=True,
        ).stdout

    def seed(self):
        (self.repo / "seed.txt").write_text("one seed\n")
        self.git("add", "seed.txt")
        self.git("commit", "-m", "Plant the seed")

    def test_new_repository_has_no_commits(self):
        garden = critters.inspect(self.repo)
        self.assertEqual((garden.branch, garden.commits, garden.recent, garden.changes), ("main", 0, 0, 0))

    def test_counts_tracked_and_untracked_changes(self):
        self.seed()
        (self.repo / "seed.txt").write_text("two seeds\n")
        (self.repo / "new\nseed.txt").write_text("a strange filename\n")
        garden = critters.inspect(self.repo)
        self.assertEqual(garden.commits, 1)
        self.assertEqual(garden.changes, 2)

    def test_rename_counts_as_one_change(self):
        self.seed()
        self.git("mv", "seed.txt", "sprout.txt")
        self.assertEqual(critters.inspect(self.repo).changes, 1)

    def test_detached_head_is_supported(self):
        self.seed()
        self.git("checkout", "--detach")
        self.assertEqual(critters.inspect(self.repo).branch, "detached HEAD")

    def test_quests_work_outside_a_repository(self):
        with tempfile.TemporaryDirectory() as other:
            result = subprocess.run(
                [sys.executable, str(Path(critters.__file__).resolve()), "--quests"],
                cwd=other,
                text=True,
                capture_output=True,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("AI eligibility unverified", result.stdout)

    def test_non_repository_gives_actionable_error(self):
        with tempfile.TemporaryDirectory() as other:
            errors = io.StringIO()
            with contextlib.redirect_stderr(errors):
                result = critters.main(["--repo", other])
        self.assertEqual(result, 1)
        self.assertIn("--demo", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
