import unittest

from parsers.markdown_extractors import extract_markdown_images, extract_markdown_links


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
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            extracted_links,
        )

    def test_extract_link_from_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        links = extract_markdown_links(text)
        self.assertListEqual([], links)

    def test_extract_image_from_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        images = extract_markdown_images(text)
        self.assertListEqual([], images)

    def test_extract_only_link(self):
        text = "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            links,
        )

    def test_extract_only_image(self):

        text = "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_images = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
            ],
            extracted_images,
        )

    def test_no_alt_text(self):
        text = "This is text with a link ![](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_images = extract_markdown_images(text)
        self.assertListEqual(
            [("", "https://www.boot.dev")],
            extracted_images,
        )
