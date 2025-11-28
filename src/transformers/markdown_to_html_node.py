from models.htmlnode import ParentNode
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
    html_node = ParentNode(tag="div", children=children)
    return html_node


def transform_text_nodes_to_html_nodes(text_nodes, parent_node_tag=None):
    html_nodes = []
    for tn in text_nodes:
        html_node = text_node_to_html_node(tn)
        if not parent_node_tag:
            html_nodes.append(html_node)
        else:
            html_nodes.append(ParentNode(tag=parent_node_tag, children=[html_node]))
    return html_nodes


def text_children(text):
    block_type = block_to_block_type(text)

    if block_type == BlockType.CODE:
        return text_to_code_html(text)
    if block_type == BlockType.HEADING:
        return text_to_heading_html(text)
    if block_type == BlockType.QUOTE:
        return text_to_quote_html(text)
    if block_type == BlockType.UNORDERED_LIST:
        return text_to_unordered_list_html(text)
    if block_type == BlockType.ORDERED_LIST:
        return text_to_ordered_list_html(text)

    # handle rest of text nodes
    text_removed_newline = " ".join(text.split("\n"))
    text_nodes = text_to_textnodes(text_removed_newline)
    html_nodes = transform_text_nodes_to_html_nodes(text_nodes)

    if block_type == BlockType.PARAGRAPH:
        return [ParentNode(tag="p", children=html_nodes)]

    return html_nodes


def text_to_heading_html(text):

    split_block = text.split(" ", 1)
    heading_text = text_to_textnodes(split_block[1])
    heading_html = transform_text_nodes_to_html_nodes(heading_text)

    tag = f"h{len(split_block[0])}"
    return [ParentNode(tag=tag, children=heading_html)]


def text_to_code_html(text):
    code_node = TextNode(text.strip("```"), text_type=TextType.CODE)
    html_node = [text_node_to_html_node(code_node)]
    return [ParentNode(tag="pre", children=html_node)]


def text_to_quote_html(text):
    quote_text = text.replace(">", "")
    text_nodes = text_to_textnodes(quote_text)
    quote_nodes = transform_text_nodes_to_html_nodes(text_nodes)
    return [ParentNode(tag="blockquote", children=quote_nodes)]


def text_to_unordered_list_html(text):
    text_removed_newline = " ".join(text.split("\n"))
    split_block = text_removed_newline.split("-")
    text_nodes = []
    for line in split_block:
        unordered_list_text = text_to_textnodes(line.strip(" "))
        text_nodes.extend(unordered_list_text)
    unordered_list_html = transform_text_nodes_to_html_nodes(text_nodes, "li")
    return [ParentNode(tag="ul", children=unordered_list_html)]


def text_to_ordered_list_html(text):
    split_block = text.split("\n")
    text_nodes = []
    for line in split_block:
        ordered_text_nodes = text_to_textnodes(line.split(" ", 1)[1])
        text_nodes.extend(ordered_text_nodes)
    ordered_list_html = transform_text_nodes_to_html_nodes(text_nodes, "li")
    return [ParentNode(tag="ol", children=ordered_list_html)]
