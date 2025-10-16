from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        txt_eq = self.text == other_node.text
        txt_type_eq = self.text_type == other_node.text_type
        url_eq = self.url == other_node.url
        return txt_eq and txt_type_eq and url_eq

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"
