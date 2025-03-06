import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return list(
        map(
            lambda block: block.strip(),
            filter(lambda block: block != "", blocks)
        )
    )


def block_to_block_type(block):
    pass
    if is_heading_block(block):
        return BlockType.HEADING
    elif is_code_block(block):
        return BlockType.CODE
    elif is_quote_block(block):
        return BlockType.QUOTE
    elif is_unordered_list_block(block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list_block(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


def is_heading_block(block):
    return re.match(r"^#{1,6}\s.+$", block)


def is_code_block(block):
    return block.startswith("```") and block.endswith("```")


def is_quote_block(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True


def is_unordered_list_block(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith("- "):
            return False
    return True


def is_ordered_list_block(block):
    lines = block.split("\n")
    i = 1
    for line in lines:
        if not line.startswith(f"{i}. "):
            return False
        i += 1
    return True
