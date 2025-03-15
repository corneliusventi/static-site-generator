import unittest

from extract_title import extract_title


class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(
            "Hello",
            extract_title("# Hello")
        )
        self.assertEqual(
            "Heading 1",
            extract_title("# Heading 1")
        )
        self.assertEqual(
            "Page Title",
            extract_title("# Page Title")
        )
