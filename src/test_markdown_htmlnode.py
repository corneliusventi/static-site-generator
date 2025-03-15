import unittest

from markdown_htmlnode import markdown_to_html_node


class TestMarkdownHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item _2_
- Item **2a**
- Item 2b
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item <i>2</i></li><li>Item <b>2a</b></li><li>Item 2b</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. Item 1
2. Item **2**
3. Item _3_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item <b>2</b></li><li>Item <i>3</i></li></ol></div>",
        )

    def test_headings(self):
        md = """
# This is a Heading h1

## This is a Heading h2

###### This is a Heading h6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a Heading h1</h1><h2>This is a Heading h2</h2><h6>This is a Heading h6</h6></div>",
        )

    def test_quote(self):
        md = """
> Markdown is a lightweight markup language **with** plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Markdown is a lightweight markup language <b>with</b> plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz. Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.</blockquote></div>",
        )
