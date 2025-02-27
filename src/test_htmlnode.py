import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        a_node = HTMLNode(
            tag="a",
            value="google.com",
            props={
                "href" : "https://google.com",
                "title" : "google.com"
            }
        )
        self.assertEqual(
            ' href="https://google.com" title="google.com"', a_node.props_to_html()
        )
        div_node = HTMLNode(
            tag="div",
            props={
                "class": "container",
            }
        )
        self.assertEqual(
            ' class="container"', div_node.props_to_html()
        )
        button_node = HTMLNode(
            tag="button",
            value="Submit",
            props={
                "type": "submit",
            }
        )
        self.assertEqual(
            ' type="submit"', button_node.props_to_html()
        )

    def test_no_props(self):
        empty_div = HTMLNode(
            tag="div",
        )
        self.assertEqual(
            "", empty_div.props_to_html()
        )

    def test_repr(self):
        button_node = HTMLNode(
            tag="button",
            value="Submit",
            props={
                "type": "submit",
            }
        )
        self.assertEqual(
            "HTMLNode(button, Submit, children=None, {'type': 'submit'})", repr(button_node)
        )

    def test_leaf_to_html_p(self):
        p_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            "<p>This is a paragraph of text.</p>", p_node.to_html()
        )

    def test_leaf_to_html_a(self):
        a_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>', a_node.to_html()
        )

    def test_leaf_to_html_no_tag(self):
        text_node = LeafNode(None, "This is a text.")
        self.assertEqual(
            "This is a text.", text_node.to_html()
        )

    def test_leaf_to_html_no_value(self):
        leaf_node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            leaf_node.to_html()


if __name__ == "__main__":
    unittest.main()
