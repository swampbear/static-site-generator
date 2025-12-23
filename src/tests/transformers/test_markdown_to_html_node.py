import unittest

from transformers.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
>This is a really cool quote
>
>Like really cool
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a really cool quote\n\nLike really cool</blockquote></div>",
        )

    def test_headings(self):
        md = """
# Title heading

## The next largest heading

### Just above the middle

#### Starting to get small here

##### Small but not smallest

###### As small as it gets

####### This should just be a paragraph
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Title heading</h1><h2>The next largest heading</h2><h3>Just above the middle</h3><h4>Starting to get small here</h4><h5>Small but not smallest</h5><h6>As small as it gets</h6><p>####### This should just be a paragraph</p></div>",
        )

    def test_unordered_list(self):
        md = """
- this is the greatest unsorted list ever
- it is undescribably unsorted
- like so unsorted


"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>this is the greatest unsorted list ever</li><li>it is undescribably unsorted</li><li>like so unsorted</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. wow, such a sorted list
2. like not unordered at all
3. that is so cool
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>wow, such a sorted list</li><li>like not unordered at all</li><li>that is so cool</li></ol></div>",
        )
