import unittest

from htmlnode import HTMLNode


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
            "HTMLNode(tag=button, value=Submit, props={'type': 'submit'}, children=None)", repr(button_node)
        )


if __name__ == "__main__":
    unittest.main()
