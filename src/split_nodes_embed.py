import re

from markdown_exptractors import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    new_nodes = []
    found_image = False
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        matches = extract_markdown_images(text)
        parts = re.split(r"\!\[.*?\]\(.*?\)", text)
        if len(parts) > 1:
            found_image = True
        for i in range(0, len(parts)):
            if parts[i] != "":
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            if i < len(parts) - 1:
                new_nodes.append(TextNode(matches[i][0], TextType.IMAGE, matches[i][1]))

    if not found_image:
        raise Exception("Error: no image found")

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    found_link = False
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        matches = extract_markdown_links(text)
        parts = re.split(r"[^!]\[.*?\]+\(.*?\)", text)
        print(parts)
        if len(parts) > 1:
            found_link = True
        for i in range(0, len(parts)):
            if parts[i] != "":
                new_nodes.append(TextNode(parts[i] + " ", TextType.TEXT))
            if i < len(parts) - 1:
                new_nodes.append(TextNode(matches[i][0], TextType.LINK, matches[i][1]))
    if not found_link:
        raise Exception("Error: no link found")

    return new_nodes
