import unittest
from src.generate.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        md = "# Title"

        title = extract_title(md)
        self.assertEqual(title, "Title")

    def test_no_title(self):
        md = "### Title"
        with self.assertRaises(Exception):
            _ = extract_title(md)

    def test_multiple_headers(self):
        md = "# Title\n## not title"
        title = extract_title(md)
        self.assertEqual(title, "Title")
