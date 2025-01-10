import unittest

from src.functions.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_eq(self):
        

        base_case = """# This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item
            
            [This is a link](https://www.example.com)
            ![This is an image](https://www.example.com/image.jpg)
            """
        



if __name__ == "__main__":
    unittest.main()