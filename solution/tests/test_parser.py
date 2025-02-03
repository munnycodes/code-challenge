import json
import unittest
from pathlib import Path

class TestPaintingParser(unittest.TestCase):
    def setUp(self):
        """Load the expected and actual JSON files before running tests."""
        expected_file = Path(__file__).parent.parent / "expected-array.json"
        actual_file = Path(__file__).parent.parent / "actual-array.json"

        with open(expected_file, "r", encoding="utf-8") as f:
            self.expected_data = json.load(f)

        with open(actual_file, "r", encoding="utf-8") as f:
            self.actual_data = json.load(f)

    def test_artworks_count(self):
        """Ensure the number of extracted artworks matches the expected count."""
        self.assertEqual(
            len(self.actual_data["artworks"]),
            len(self.expected_data["artworks"]),
            "Mismatch in number of artworks extracted."
        )

    def test_artwork_fields(self):
        """Check that each extracted artwork has the required fields."""
        required_fields = {"name", "link", "image"}
        optional_fields = {"extensions"}

        # Check for missing required fields
        for artwork in self.actual_data["artworks"]:
            missing_fields = required_fields - artwork.keys()
            self.assertFalse(missing_fields, f"Missing required fields: {missing_fields} in {artwork}")

            # Check for optional fields
            missing_optional_fields = optional_fields - artwork.keys()
        # Comment or remove this line to suppress optional field warnings
            # if missing_optional_fields:
            #     print(f"Missing optional fields: {missing_optional_fields} in {artwork}")

    def test_artwork_content(self):
        """Compare extracted artwork details with expected values."""
        for actual, expected in zip(self.actual_data["artworks"], self.expected_data["artworks"]):
            for key in expected:
                self.assertEqual(actual[key], expected[key], f"Mismatch in field '{key}' for artwork: {actual.get('name', 'Unknown')}")


if __name__ == "__main__":
    unittest.main()
