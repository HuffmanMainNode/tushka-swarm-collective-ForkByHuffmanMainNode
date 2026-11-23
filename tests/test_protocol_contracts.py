import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "spec" / "v1"


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


class ProtocolContractTests(unittest.TestCase):
    def test_schema_documents_are_draft_2020_12_objects(self):
        for name in ("task.schema.json", "result.schema.json"):
            with self.subTest(schema=name):
                schema = load_json(SPEC / name)
                self.assertEqual(
                    schema["$schema"],
                    "https://json-schema.org/draft/2020-12/schema",
                )
                self.assertEqual(schema["type"], "object")
                self.assertFalse(schema["additionalProperties"])

    def test_task_fixture_matches_required_contract_fields(self):
        schema = load_json(SPEC / "task.schema.json")
        fixture = load_json(SPEC / "examples" / "task.json")
        self.assertEqual(fixture["protocol_version"], "1.0")
        self.assertEqual(fixture["message_type"], "task")
        self.assertTrue(all(key in fixture for key in schema["required"]))
        self.assertEqual(set(fixture), set(schema["properties"]))

    def test_success_fixture_has_content_and_no_error(self):
        schema = load_json(SPEC / "result.schema.json")
        fixture = load_json(SPEC / "examples" / "result-success.json")
        self.assertTrue(all(key in fixture for key in schema["required"]))
        self.assertEqual(fixture["protocol_version"], "1.0")
        self.assertEqual(fixture["message_type"], "result")
        self.assertEqual(fixture["status"], "succeeded")
        self.assertIn("content", fixture)
        self.assertNotIn("error", fixture)
        self.assertEqual(set(fixture) - set(schema["properties"]), set())

    def test_failure_fixture_has_structured_error(self):
        schema = load_json(SPEC / "result.schema.json")
        fixture = load_json(SPEC / "examples" / "result-failure.json")
        self.assertTrue(all(key in fixture for key in schema["required"]))
        self.assertEqual(fixture["status"], "failed")
        self.assertIn("code", fixture["error"])
        self.assertIn("message", fixture["error"])
        self.assertEqual(set(fixture) - set(schema["properties"]), set())


if __name__ == "__main__":
    unittest.main()
