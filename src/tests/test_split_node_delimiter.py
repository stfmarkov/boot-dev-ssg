import unittest

from src.classes.text_node import TextNode, TextType
from src.functions.split_nodes_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):

        code_block = TextNode("This is text with a `code block` word", TextType.NORMAL.value)
        code_block_nodes = split_nodes_delimiter([code_block], "`", TextType.CODE.value)

        code_block_one = TextNode("This is text with a ", TextType.NORMAL.value)
        code_block_two = TextNode("code block", TextType.CODE.value)
        code_block_three = TextNode(" word", TextType.NORMAL.value)

        self.assertEqual(code_block_nodes[0].text, code_block_one.text)
        self.assertEqual(code_block_nodes[1].text, code_block_two.text)
        self.assertEqual(code_block_nodes[2].text, code_block_three.text)

        self.assertEqual(code_block_one.text_type, code_block_nodes[0].text_type)
        self.assertEqual(code_block_two.text_type, code_block_nodes[1].text_type)
        self.assertEqual(code_block_three.text_type, code_block_nodes[2].text_type)

        bold = TextNode("This is text with a **bold** word", TextType.NORMAL.value)
        bold_nodes = split_nodes_delimiter([bold], "**", TextType.CODE.value)

        bold_one = TextNode("This is text with a ", TextType.NORMAL.value)
        bold_two = TextNode("bold", TextType.CODE.value)
        bold_three = TextNode(" word", TextType.NORMAL.value)

        self.assertEqual(bold_nodes[0].text, bold_one.text)
        self.assertEqual(bold_nodes[1].text, bold_two.text)
        self.assertEqual(bold_nodes[2].text, bold_three.text)

        self.assertEqual(bold_one.text_type, bold_nodes[0].text_type)
        self.assertEqual(bold_two.text_type, bold_nodes[1].text_type)
        self.assertEqual(bold_three.text_type, bold_nodes[2].text_type)

        no_delimiter = TextNode("This is text with no bold word", TextType.NORMAL.value)
        no_delimiter_nodes = split_nodes_delimiter([no_delimiter], "**", TextType.NORMAL)

        no_delimiter_one = TextNode("This is text with no bold word", TextType.NORMAL.value)

        self.assertEqual(no_delimiter_nodes[0].text, no_delimiter_one.text)

        not_specified = TextNode("This is text with a **bold** word", TextType.NORMAL.value)
    
        with self.assertRaises(ValueError):
            split_nodes_delimiter([not_specified], "", TextType.BOLD)

        

if __name__ == "__main__":
    unittest.main()