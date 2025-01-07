import unittest

from html_parent_node import HTMLParentNode
from html_leaf_node import HTMLLeafNode



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        empty = HTMLParentNode(tag="a", children=None, props={'href': 'https://www.example.com'})
        
        p = HTMLParentNode(
            "p",
            [
                HTMLLeafNode("b", "Bold text"),
                HTMLLeafNode(None, "Normal text"),
                HTMLLeafNode("i", "italic text"),
                HTMLLeafNode(None, "Normal text"),
            ],
        )

        div = HTMLParentNode(
            tag='div',
            children=[p, HTMLLeafNode(None, "Normal text")],
        )

        no_tag = HTMLParentNode( None, [HTMLLeafNode("b", "Bold text")])


        self.assertRaises(ValueError, empty.to_html)

        self.assertEqual(
            p.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
        )

        self.assertEqual(
            div.to_html(),
            '<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>Normal text</div>',
        )

        self.assertRaises(ValueError, no_tag.to_html)



if __name__ == "__main__":
    unittest.main()