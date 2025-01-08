import unittest

from src.functions.extract_markdown_links import extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        base_case = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        base_case_extraction = extract_markdown_links(base_case)

        self.assertEqual(base_case_extraction[0], ("to boot dev", "https://www.boot.dev"))
        self.assertEqual(base_case_extraction[1], ("to youtube", "https://www.youtube.com/@bootdotdev"))

        no_links = "This is text with no links"
        no_links_extraction = extract_markdown_links(no_links)

        self.assertEqual(no_links_extraction, [])

        no_text = "This is text with a ![](https://www.boot.dev)"
        no_text_extraction = extract_markdown_links(no_text)

        self.assertEqual(no_text_extraction[0], ("", "https://www.boot.dev"))



if __name__ == "__main__":
    unittest.main()