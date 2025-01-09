import unittest

from src.functions.markdown_to_blocks import markdown_to_blocks
from src.classes.text_node import TextNode, TextType


class TestMarkdownToBlocks(unittest.TestCase):
    def test_eq(self):
        
        base_case = """# This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item"""
        
        blocks = markdown_to_blocks(base_case)

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block",
            "* This is a list item",
            "* This is another list item"
        ]

        self.assertEqual(blocks, expected)

        empty_lines = """# This is a heading

        

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item

            """
        
        blocks = markdown_to_blocks(empty_lines)

        self.assertEqual(blocks, expected)
        
if __name__ == "__main__":
    unittest.main()