from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.HEADING:
            parts = block.split(" ", maxsplit=1)
            tag = f"h{len(parts[0])}"
            return ParentNode(tag, text_to_children(parts[1]))
        case BlockType.CODE:
            text = block.strip("```").lstrip()
            text_node = TextNode(text, TextType.TEXT)
            child = text_node_to_html_node(text_node)
            code = ParentNode("code", [child])
            return ParentNode("pre", [code])
        case BlockType.QUOTE:
            lines = block.split("\n")
            lines = map(lambda line: line.lstrip(">").strip(), lines)
            text = " ".join(lines)
            return ParentNode("blockquote", text_to_children(text))
        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            children = []
            for line in lines:
                parts = line.split(" ", maxsplit=1)
                children.append(
                    ParentNode("li", text_to_children(parts[1]))
                )
            return ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            children = []
            for line in lines:
                parts = line.split(" ", maxsplit=1)
                children.append(
                    ParentNode("li", text_to_children(parts[1]))
                )
            return ParentNode("ol", children)
        case BlockType.PARAGRAPH:
            lines = block.split("\n")
            text = " ".join(lines)
            return ParentNode("p", text_to_children(text))
        case _:
            raise Exception()


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(
        map(lambda text_node: text_node_to_html_node(text_node), text_nodes)
    )
