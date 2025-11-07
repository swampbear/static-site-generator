from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_embed import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    textnode = TextNode(text, TextType.TEXT)
    new_nodes = [textnode]
    delimiters = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}
    for delimiter in delimiters:
        new_nodes = split_nodes_delimiter(new_nodes, delimiter, delimiters[delimiter])
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes
