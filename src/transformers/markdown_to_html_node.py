from models.htmlnode import HTMLNode, LeafNode, ParentNode
from models.textnode import TextNode, TextType, text_node_to_html_node
from parsers.block_to_block_type import BlockType, block_to_block_type
from parsers.markdown_to_blocks import markdown_to_blocks
from transformers.text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        children_node = text_children(block)
        children.extend(children_node)
    return ParentNode(tag="div", children=children)


def text_children(text):
    block_type = block_to_block_type(text)

    # codeblock has special syntax and is handled manually
    if block_type == BlockType.CODE:
        code_node = TextNode(text.strip("```"), text_type=TextType.CODE)
        html_node = [text_node_to_html_node(code_node)]
        return [ParentNode(tag="pre", children=html_node)]

    # handle rest of text nodes
    text = " ".join(text.split("\n"))

    text_nodes = text_to_textnodes(text)
    html_nodes = []  # for gathering all children of block
    for tn in text_nodes:
        html_node = text_node_to_html_node(tn)
        html_nodes.append(html_node)

    if block_type == BlockType.PARAGRAPH:
        return [ParentNode(tag="p", children=html_nodes)]
    if block_type == BlockType.HEADING:
        split_block = text.split(
            " ", 1
        )  # splits the header block into hashtags and content : [#, This is a header
        heading_text = text_to_textnodes(split_block[1])
        heading_html = []
        for tn in heading_text:
            heading_html_node = text_node_to_html_node(tn)
            heading_html.append(heading_html_node)

        tag = f"h{len(split_block[0])}"
        return [ParentNode(tag=tag, children=heading_html)]
    if block_type == BlockType.UNORDERED_LIST:
        split_block = text.split(
            "-"
        )  # splits the header block into hashtags and content : [#, This is a header
        text_nodes = []
        for line in split_block:
            unordered_list_text = text_to_textnodes(line.strip(" "))
            text_nodes.extend(unordered_list_text)
        unordered_list_html = []
        for tn in text_nodes:
            unordered_list_html_node = text_node_to_html_node(tn)
            unordered_list_html.append(
                ParentNode(tag="li", children=[unordered_list_html_node])
            )

        return [ParentNode(tag="ul", children=unordered_list_html)]

    return html_nodes
