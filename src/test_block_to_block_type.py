import unittest

from block_to_block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks


class TestBlockToBlockTypes(unittest.TestCase):
    def test_heading(self):
        md = """
# This is a heading

## This is a heading

### This is a heading

#### This is a heading

##### This is a heading

###### This is a heading

"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(BlockType.HEADING, block_type)

    def test_to_long_heading(self):
        md = """
        ####### This heading is one to long

        ################# this is just way to long
        """
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0])
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_quote(self):
        md = """
> This is a quote
> This is also a quote
"""
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_code(self):
        md = """
```print("this is a code block")```
            """
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.CODE, block_type)

    def test_unordered_list(self):
        md = """
- this list is so unordered
- unordered list entry
- you know the drill
            """
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_ordered_list(self):
        md = """
1. number one
2. number two
3. and so on
4. and so on
5. and so on
6. and so on
7. and so on
8. and so on
9. and so on
10. and so on
11. and so on
            """
        blocks = markdown_to_blocks(md)
        block_type = block_to_block_type(blocks[0])
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_paragraph(self):
        md = """
This is just some standard
normal, paragraphs

nothing to see here, nothing fancy
just paragraphs
        """
        blocks = markdown_to_blocks(md)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_imperfect_blocks(self):
        md = """
        #Almost a header

        ```print("not quite a code block")``

        > Cool quote broo
        or not

        - to be
        -or not to be a unordered list

        1. one
        3. not 2

        1. one
        2.two little space
        """
        blocks = markdown_to_blocks(md)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(BlockType.PARAGRAPH, block_type)
