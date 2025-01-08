import unittest

from src.classes.htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        heading = HTMLNode('h1', 'This is a text node')
        link = HTMLNode('a', 'This is a link', props={'href': 'https://www.example.com'})
        div = HTMLNode(tag='div', children=[heading, link])

        self.assertEqual(link.props_to_html(), 'href="https://www.example.com"')
        self.assertEqual(div.children, [heading, link])
        self.assertEqual(heading.tag, 'h1')



if __name__ == "__main__":
    unittest.main()