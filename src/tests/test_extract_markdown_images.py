import unittest

from src.functions.extract_markdown_images import extract_markdown_images


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        base_case = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        base_case_extraction = extract_markdown_images(base_case)

        self.assertEqual(base_case_extraction[0], ("rick roll", "https://i.imgur.com/aKaOqIh.gif"))
        self.assertEqual(base_case_extraction[1], ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"))

        no_images = "This is text with no images"
        no_images_extraction = extract_markdown_images(no_images)

        self.assertEqual(no_images_extraction, [])

        no_text = "This is text with a ![](https://i.imgur.com/aKaOqIh.gif)"
        no_text_extraction = extract_markdown_images(no_text)

        self.assertEqual(no_text_extraction[0], ("", "https://i.imgur.com/aKaOqIh.gif"))



if __name__ == "__main__":
    unittest.main()