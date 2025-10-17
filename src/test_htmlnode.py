import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
