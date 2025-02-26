import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_normal(self):
        node = TextNode("This is a normal text node", TextType.TEXT)
        node2 = TextNode("This is a normal text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_not_eq_normal(self):
        node = TextNode("This is a normal text node #1", TextType.TEXT)
        node2 = TextNode("This is a normal text node #2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("google.com", TextType.LINK, "https://google.com")
        node2 = TextNode("google.com", TextType.LINK, "https://google.com")
        self.assertEqual(node, node2)

    def test_not_eq_link(self):
        node = TextNode("google.com", TextType.LINK, "https://google.com")
        node2 = TextNode("apple.com", TextType.LINK, "https://apple.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
