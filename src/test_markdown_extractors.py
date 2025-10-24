import unittest

from markdown_exptractors import extract_markdown_images, extract_markdown_links


class TestMarkdownExtractors(unittest.TestCase):

    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            extracted_images,
        )

    def test_extract_link(self):
        text = "This is a [link](jobjorn.com)"
        extracted_links = extract_markdown_links(text)
        self.assertListEqual([("link", "jobjorn.com")], extracted_links)
