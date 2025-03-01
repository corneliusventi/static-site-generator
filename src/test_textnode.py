import unittest

from textnode import TextNode, TextType, split_nodes_delimiter, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is normal text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is normal text")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")

    def test_link(self):
        node = TextNode("This is link", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is link")
        self.assertEqual(html_node.props, {"href": "https://google.com"})

    def test_image(self):
         node = TextNode("This is image", TextType.IMAGE, "https://google.com")
         html_node = text_node_to_html_node(node)
         self.assertEqual(html_node.tag, "img")
         self.assertEqual(html_node.value, None)
         self.assertEqual(html_node.props, {"src": "https://google.com", "alt": "This is image"})

    def test_split_nodes_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_bold(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle", TextType.TEXT),
            ]
        )

    def test_split_nodes_italic(self):
        node = TextNode("This is text with a _italic phrase_ in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic phrase", TextType.ITALIC),
                TextNode(" in the middle", TextType.TEXT),
            ]
        )


if __name__ == "__main__":
    unittest.main()
