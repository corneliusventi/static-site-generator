import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type, BlockType
)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multiple(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

This is yet another **bolded** paragraph

Another paragraph with _italic_ words and some `inline code`
Still part of the same paragraph on a new line

- Another list
- with more items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                "This is yet another **bolded** paragraph",
                "Another paragraph with _italic_ words and some `inline code`\nStill part of the same paragraph on a new line",
                "- Another list\n- with more items",
            ],
        )

    def test_heading_block(self):
        self.assertEqual(
            block_to_block_type("# Heading 1"),
            BlockType.HEADING
        )
        self.assertEqual(
            block_to_block_type("## Heading 2"),
            BlockType.HEADING
        )
        self.assertEqual(
            block_to_block_type("### Heading 3"),
            BlockType.HEADING
        )

    def test_code_block(self):
        block = """
```
function test() {
    console.log("notice the blank line before this function?");
}
```
"""
        self.assertEqual(
            block_to_block_type(block.strip()),
            BlockType.CODE
        )

    def test_quote_block(self):
        block = """
> First line
> Another line
>
> > Nested line
>
> Last line
"""
        self.assertEqual(
            block_to_block_type(block.strip()),
            BlockType.QUOTE
        )

    def test_unordered_list_block(self):
        block = """
- First line
- Another line
- Nested line
- Last line
"""
        self.assertEqual(
            block_to_block_type(block.strip()),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list_block(self):
        block = """
1. First line
2. Another line
3. Nested line
4. Last line
"""
        self.assertEqual(
            block_to_block_type(block.strip()),
            BlockType.ORDERED_LIST
        )

    def test_paragraph_block(self):
        block = """
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        self.assertEqual(
            block_to_block_type(block.strip()),
            BlockType.PARAGRAPH
        )
