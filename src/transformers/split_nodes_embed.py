import re

from parsers.markdown_extractors import extract_markdown_images, extract_markdown_links
from models.textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        matches = extract_markdown_images(text)
        parts = re.split(r"\!\[.*?\]\(.*?\)", text)
        for i in range(0, len(parts)):
            if parts[i] != "":
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            if i < len(parts) - 1:
                if matches[i][0]:
                    new_nodes.append(
                        TextNode(matches[i][0], TextType.IMAGE, matches[i][1])
                    )

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        matches = extract_markdown_links(text)
        parts = re.split(r"(?<!!)\[.*?\]+\(.*?\)", text)
        for i in range(0, len(parts)):
            if parts[i] != "":
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            if i < len(parts) - 1:
                if matches[i][0] != "":
                    new_nodes.append(
                        TextNode(matches[i][0], TextType.LINK, matches[i][1])
                    )

    return new_nodes
