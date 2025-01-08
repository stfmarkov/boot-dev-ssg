import unittest

from src.classes.text_node import TextNode, TextType
from src.functions.text_node_to_html import text_node_to_html
from src.classes.html_leaf_node import HTMLLeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        normal_node = TextNode("This is a text node", TextType.NORMAL)
        bold_node = TextNode("This is a text node", TextType.BOLD)
        italic_node = TextNode("This is a text node", TextType.ITALIC)
        code_node = TextNode("This is a text node", TextType.CODE)
        link_node = TextNode("This is a text node", TextType.LINK, "https://www.example.com")
        image_node = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com")

        normal_leaf = HTMLLeafNode(None, "This is a text node")
        bold_leaf = HTMLLeafNode('b', "This is a text node")
        italic_leaf = HTMLLeafNode('i', "This is a text node")
        code_leaf = HTMLLeafNode('code', "This is a text node")
        link_leaf = HTMLLeafNode('a', "This is a text node", props={'href': "https://www.example.com"})
        image_leaf = HTMLLeafNode('img', None, props={'src': "https://www.example.com"})

        html_normal_leaf_node = text_node_to_html(normal_node)
        html_bold_leaf_node = text_node_to_html(bold_node)
        html_italic_leaf_node = text_node_to_html(italic_node)
        html_code_leaf_node = text_node_to_html(code_node)
        html_link_leaf_node = text_node_to_html(link_node)
        html_image_leaf_node = text_node_to_html(image_node)

        self.assertEqual(html_normal_leaf_node.props_to_html(), normal_leaf.props_to_html())
        self.assertEqual(html_bold_leaf_node.props_to_html(), bold_leaf.props_to_html())
        self.assertEqual(html_italic_leaf_node.props_to_html(), italic_leaf.props_to_html())
        self.assertEqual(html_code_leaf_node.props_to_html(), code_leaf.props_to_html())
        self.assertEqual(html_link_leaf_node.props_to_html(), link_leaf.props_to_html())
        self.assertEqual(html_image_leaf_node.props_to_html(), image_leaf.props_to_html())

if __name__ == "__main__":
    unittest.main()