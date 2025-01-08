import unittest

from src.classes.text_node import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.NORMAL, "https://www.example.com")

        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertIsNone(node.url)
        self.assertIsNotNone(node3.url)



if __name__ == "__main__":
    unittest.main()