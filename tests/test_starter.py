import importlib.util
import json
import tempfile
import tomllib
import unittest
from pathlib import Path

MODULE = Path(__file__).parents[1] / "starter.py"
spec = importlib.util.spec_from_file_location("starter", MODULE)
starter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(starter)
REF = "a" * 40


class AdoptionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def configure(self, apply=False):
        return starter.configure(self.root, REF, apply=apply)

    def test_preview_never_writes(self):
        result = self.configure()
        self.assertEqual(list(self.root.iterdir()), [])
        self.assertEqual(result["status"], "preview")
        self.assertIn(".codex/config.toml", result["writes"])

    def test_second_adoption_is_noop(self):
        self.configure(True)
        before = {
            p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()
        }
        result = self.configure(True)
        after = {
            p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()
        }
        self.assertEqual(before, after)
        self.assertEqual(result["writes"], [])

    def test_preserves_existing_instructions_and_config(self):
        (self.root / "AGENTS.md").write_text("Existing project authority.\n")
        (self.root / ".codex").mkdir()
        config = self.root / ".codex/config.toml"
        config.write_text('model = "example"\n# Keep this comment.\n')
        self.configure(True)
        self.assertEqual((self.root / "AGENTS.md").read_text(), "Existing project authority.\n")
        self.assertTrue(config.read_text().startswith('model = "example"\n# Keep this comment.\n'))
        self.assertIn("AGENTS.skills-first.md", starter.configure(self.root, REF)["present"])

    def test_conflict_blocks_all_writes(self):
        (self.root / ".codex").mkdir()
        p = self.root / ".codex/config.toml"
        p.write_text('[plugins."gz-skills@skills-first-starter"]\nenabled = false\n')
        with self.assertRaises(starter.AdoptionError):
            self.configure(True)
        self.assertFalse((self.root / ".skills-first").exists())
        self.assertFalse((self.root / "AGENTS.md").exists())
        self.assertIn("false", p.read_text())

    def test_gzkit_is_not_reconfigured(self):
        (self.root / ".gzkit").mkdir()
        with self.assertRaises(starter.AdoptionError):
            self.configure(True)
        self.assertEqual([p.name for p in self.root.iterdir()], [".gzkit"])

    def test_symlink_destination_is_rejected(self):
        external = self.root / "outside"
        external.mkdir()
        (self.root / ".codex").symlink_to(external, target_is_directory=True)
        with self.assertRaises(starter.AdoptionError):
            self.configure(True)
        self.assertEqual(list(external.iterdir()), [])

    def test_existing_legacy_skill_copy_blocks_duplicate_discovery(self):
        p = self.root / ".agents/skills/gzs-router"
        p.mkdir(parents=True)
        (p / "SKILL.md").write_text("Legacy skill copy")
        with self.assertRaises(starter.AdoptionError):
            self.configure(True)
        self.assertFalse((self.root / ".codex").exists())

    def test_existing_other_marketplace_plugin_blocks_duplicate(self):
        (self.root / ".codex").mkdir()
        (self.root / ".codex/config.toml").write_text(
            '[plugins."superpowers@other"]\nenabled = true\n'
        )
        with self.assertRaises(starter.AdoptionError):
            self.configure(True)

    def test_pending_profile_is_not_a_readiness_claim(self):
        self.configure(True)
        self.assertFalse((self.root / ".gz-skills/settings.json").exists())
        self.assertEqual(starter.status(self.root)["runtime_readiness"], "unverified")

    def test_existing_profile_and_rules_are_preserved(self):
        (self.root / ".gz-skills").mkdir()
        p = self.root / ".gz-skills/settings.json"
        p.write_text('{"schema_version": 1, "profile": "lite"}\n')
        self.configure(True)
        self.assertEqual(p.read_text(), '{"schema_version": 1, "profile": "lite"}\n')

    def test_malformed_settings_do_not_get_overwritten(self):
        (self.root / ".gz-skills").mkdir()
        (self.root / ".gz-skills/settings.json").write_text("{}")
        with self.assertRaises(starter.AdoptionError):
            self.configure(True)

    def test_backplane_is_pinned_but_disabled(self):
        self.configure(True)
        data = tomllib.loads((self.root / ".codex/config.toml").read_text())
        self.assertIs(
            data["plugins"]["superpowers-backplane@skills-first-starter"]["enabled"], False
        )
        self.assertIs(data["plugins"]["superpowers@skills-first-starter"]["enabled"], True)
        self.assertIs(data["plugins"]["gz-skills@skills-first-starter"]["enabled"], True)

    def test_active_backplane_is_not_silently_disabled(self):
        (self.root / ".codex").mkdir()
        p = self.root / ".codex/config.toml"
        original = '[plugins."superpowers-backplane@skills-first-starter"]\nenabled = true\n'
        p.write_text(original)
        with self.assertRaises(starter.AdoptionError):
            self.configure(True)
        self.assertEqual(p.read_text(), original)
        self.assertFalse((self.root / ".skills-first").exists())

    def test_frontdoor_is_present_and_modified_skill_is_preserved(self):
        self.configure(True)
        skill = self.root / ".agents/skills/skills-first-start/SKILL.md"
        self.assertTrue(skill.is_file())
        skill.write_text("Project-specific routing")
        with self.assertRaises(starter.AdoptionError):
            self.configure(True)
        self.assertEqual(skill.read_text(), "Project-specific routing")

    def test_backport_assessment_preserves_records_and_does_not_follow_links(self):
        (self.root / "records").mkdir()
        record = self.root / "records/private.txt"
        record.write_text("private fixture content")
        (self.root / "alias").symlink_to(self.root / "records", target_is_directory=True)
        before = record.read_bytes()
        result = starter.backport(self.root)
        self.assertEqual(result["writes"], [])
        self.assertEqual(result["backplane"], "deferred")
        self.assertNotIn("private fixture content", json.dumps(result))
        self.assertNotIn("private.txt", json.dumps(result))
        self.assertEqual(record.read_bytes(), before)
        self.assertEqual({x.name for x in self.root.iterdir()}, {"records", "alias"})
        self.assertEqual(
            next(e for e in result["inventory"] if e["path"] == "alias")["kind"], "symlink"
        )

    def test_other_frontdoor_discovery_is_not_duplicated(self):
        (self.root / ".codex/skills/skills-first-start").mkdir(parents=True)
        with self.assertRaises(starter.AdoptionError):
            self.configure(True)
        self.assertFalse((self.root / ".agents").exists())

    def test_backport_inventory_is_bounded(self):
        for n in range(205):
            (self.root / f"entry-{n}").touch()
        result = starter.backport(self.root)
        self.assertEqual(len(result["inventory"]), 200)
        self.assertTrue(result["inventory_truncated"])

    def test_pins_are_immutable_and_marketplace_matches(self):
        starter.validate_bundle()
        catalog = json.loads((MODULE.parent / ".agents/plugins/marketplace.json").read_text())
        self.assertEqual(
            {p["name"]: p["source"]["ref"] for p in catalog["plugins"]},
            {p["name"]: p["revision"] for p in starter.bundle()["components"]},
        )

    def test_moving_starter_ref_is_rejected(self):
        with self.assertRaises(starter.AdoptionError):
            starter.configure(self.root, "main", apply=True)


if __name__ == "__main__":
    unittest.main()
