import unittest

from transformers.split_nodes_delimiter import split_nodes_delimiter
from models.textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            TextNode("This is text with a ", TextType.TEXT, None), new_nodes[0]
        )

    def test_italic(self):
        node = TextNode("I love _italians_, I mean it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(TextNode("italians", TextType.ITALIC, None), new_nodes[1])

    def test_bold(self):
        node = TextNode("That is pretty **bold** of you", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(TextNode("bold", TextType.BOLD, None), new_nodes[1])

    def test_multiple_inline(self):
        node = TextNode(
            "This is text with a `code block``word`, and this is `another`",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            TextNode("This is text with a ", TextType.TEXT, None), new_nodes[0]
        )
        self.assertEqual(TextNode("code block", TextType.CODE, None), new_nodes[1])
        self.assertEqual(TextNode("word", TextType.CODE, None), new_nodes[3])
        self.assertEqual(TextNode("another", TextType.CODE, None), new_nodes[5])

    def test_start_of_node(self):
        node = TextNode("**bold** of you sir", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(TextNode("bold", TextType.BOLD, None), new_nodes[1])

    def test_end_of_node(self):
        node = TextNode("You are not _italian_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(TextNode("italian", TextType.ITALIC, None), new_nodes[1])

    def test_only_one_delimieter(self):
        node = TextNode("Hold the _door", TextType.TEXT)
        with self.assertRaises(Exception):
            _ = split_nodes_delimiter([node], "_", TextType.ITALIC)
