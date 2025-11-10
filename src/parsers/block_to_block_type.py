from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    prefix = block[0]
    if prefix == "#":
        header = block.split(" ")[0]
        if header == len(header) * "#" and len(header) <= 6:
            return BlockType.HEADING

    if prefix == ">":
        lines = block.split("\n")
        for line in lines:
            if line[0] != ">":
                return BlockType.PARAGRAPH

        return BlockType.QUOTE
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE

    if block[:2] == "- ":
        lines = block.split("\n")
        for line in lines:
            if line[:2] != "- ":
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    if block[:3] == "1. ":
        lines = block.split("\n")
        for i in range(0, len(lines)):
            if lines[i].split(" ")[0] != f"{i+1}.":
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
