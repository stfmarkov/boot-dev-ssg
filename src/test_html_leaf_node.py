import unittest

from html_leaf_node import HTMLLeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        p = HTMLLeafNode('p', 'This is a text node')
        a = HTMLLeafNode('a', 'This is a link', props={'href': 'https://www.example.com'})
        empty = HTMLLeafNode('a', None, props={'href': 'https://www.example.com'})

        self.assertEqual(p.to_html(), '<p>This is a text node</p>')
        self.assertEqual(a.to_html(), '<a href="https://www.example.com">This is a link</a>')

        self.assertRaises(ValueError, empty.to_html)



if __name__ == "__main__":
    unittest.main()