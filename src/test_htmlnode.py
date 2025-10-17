import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        tag = "p"
        value = "hello world"
        children = None
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        target_props_html = ' href="https://www.google.com" target="_blank"'

        node = HTMLNode(
            tag,
            value,
            children,
            props,
        )
        self.assertEqual(node.props_to_html(), target_props_html)

    def test_values(self):
        tag = "p"
        value = "hello world"
        children = None
        props = None

        node = HTMLNode(
            tag,
            value,
            children,
            props,
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "hello world")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        tag = "p"
        value = "hello world"
        children = None
        props = None

        node = HTMLNode(
            tag,
            value,
            children,
            props,
        )

        expected_repr = (
            'HTMLNode(tag="p", value="hello world", children=None, props=None)'
        )
        self.assertEqual(node.__repr__(), expected_repr)

    def test_leafnode(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafnode_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_no_value_leafnode(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag_leafnode(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
