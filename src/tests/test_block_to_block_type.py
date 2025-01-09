import unittest

from src.functions.block_to_block_type import block_to_block_type


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        heading = "# This is a heading"
        code = "```python\nprint('Hello, World!')\n```"
        quote = "> This is a quote \n> This is another quote"
        unordered_list = "* This is a list item"
        ordered_list = "1. This is a list item \n2. This is another list item"
        paragraph = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."

        not_heading = "This is not a heading"
        not_code = "```This is not code"
        not_quote = "> This is not a quote\nThis is a quote"
        not_unordered_list = "* This is a list item\nThis is not a list item"
        not_ordered_list = "1. This is a list item \n3. This is not another list item"

        self.assertEqual(block_to_block_type(heading), 'heading')
        self.assertEqual(block_to_block_type(code), 'code')
        self.assertEqual(block_to_block_type(quote), 'quote')
        self.assertEqual(block_to_block_type(unordered_list), 'unordered_list')
        self.assertEqual(block_to_block_type(ordered_list), 'ordered_list')
        self.assertEqual(block_to_block_type(paragraph), 'paragraph')

        self.assertEqual(block_to_block_type(not_heading), 'paragraph')
        self.assertEqual(block_to_block_type(not_code), 'paragraph')
        self.assertEqual(block_to_block_type(not_quote), 'paragraph')
        self.assertEqual(block_to_block_type(not_unordered_list), 'paragraph')
        self.assertEqual(block_to_block_type(not_ordered_list), 'paragraph')


if __name__ == "__main__":
    unittest.main()