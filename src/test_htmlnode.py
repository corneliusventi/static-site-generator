import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_multiple_children(self):
        child_node_1 = LeafNode("h1", "heading")
        child_node_2 = LeafNode("p", "paragraph")
        child_node_3 = LeafNode("span", "test")
        parent_node = ParentNode("div", [child_node_1, child_node_2, child_node_3])
        self.assertEqual(parent_node.to_html(), "<div><h1>heading</h1><p>paragraph</p><span>test</span></div>")

    def test_parent_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_parent_to_html_with_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, child_node)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
