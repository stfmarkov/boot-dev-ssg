import unittest

from text_node import TextNode, TextType
from functions.split_nodes_delimiter import split_nodes_delimiter
from html_leaf_node import HTMLLeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        code_block = TextNode("This is text with a `code block` word", TextType.NORMAL)
        code_block_nodes = split_nodes_delimiter([code_block], "`", TextType.CODE)

        code_block_one = TextNode("This is text with a ", TextType.NORMAL)
        code_block_two = TextNode("code block", TextType.CODE)
        code_block_three = TextNode(" word", TextType.NORMAL)

        self.assertEqual(code_block_nodes[0].text, code_block_one.text)
        self.assertEqual(code_block_nodes[1].text, code_block_two.text)
        self.assertEqual(code_block_nodes[2].text, code_block_three.text)

        self.assertEqual(code_block_one.text_type, code_block_nodes[0].text_type)
        self.assertEqual(code_block_two.text_type, code_block_nodes[1].text_type)
        self.assertEqual(code_block_three.text_type, code_block_nodes[2].text_type)

        bold = TextNode("This is text with a **bold** word", TextType.NORMAL)
        bold_nodes = split_nodes_delimiter([bold], "**", TextType.CODE)

        bold_one = TextNode("This is text with a ", TextType.NORMAL)
        bold_two = TextNode("bold", TextType.CODE)
        bold_three = TextNode(" word", TextType.NORMAL)

        self.assertEqual(bold_nodes[0].text, bold_one.text)
        self.assertEqual(bold_nodes[1].text, bold_two.text)
        self.assertEqual(bold_nodes[2].text, bold_three.text)

        self.assertEqual(bold_one.text_type, bold_nodes[0].text_type)
        self.assertEqual(bold_two.text_type, bold_nodes[1].text_type)
        self.assertEqual(bold_three.text_type, bold_nodes[2].text_type)

        no_delimiter = TextNode("This is text with no bold word", TextType.NORMAL)
        no_delimiter_nodes = split_nodes_delimiter([no_delimiter], "**", TextType.NORMAL)

        no_delimiter_one = TextNode("This is text with no bold word", TextType.NORMAL)

        self.assertEqual(no_delimiter_nodes[0].text, no_delimiter_one.text)

        not_specified = TextNode("This is text with a **bold** word", TextType.NORMAL)
    
        with self.assertRaises(ValueError):
            split_nodes_delimiter([not_specified], "", TextType.BOLD)

        

if __name__ == "__main__":
    unittest.main()