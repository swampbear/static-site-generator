import re

from markdown_exptractors import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        matches = extract_markdown_images(text)
        splt = re.split(r"\!\[.*?\]\(.*?\)", text)
        for i in range(0, len(splt)):
            if splt[i] != "":
                new_nodes.append(TextNode(splt[i], TextType.TEXT))
            if i < len(splt) - 1:
                new_nodes.append(TextNode(matches[i][0], TextType.IMAGE, matches[i][1]))

    return new_nodes


def split_nodes_link(old_nodes):
    pass
