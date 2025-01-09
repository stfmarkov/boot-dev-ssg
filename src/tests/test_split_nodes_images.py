import unittest

from src.functions.split_nodes_images import split_nodes_images
from src.classes.text_node import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):
    def test_eq(self):

        base_case = TextNode(
            "This is text with an image ![alt text](https://www.boot.dev/image.png). A verty cool image",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_images([base_case])

        self.assertEqual(new_nodes[0].text, "This is text with an image !")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL.value)

        self.assertEqual(new_nodes[1].text, "alt text")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK.value)
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev/image.png")

        self.assertEqual(new_nodes[2].text, ". A verty cool image")
        self.assertEqual(new_nodes[2].text_type, TextType.NORMAL.value)
        
        no_images = TextNode(
            "This is text with no images",
            TextType.NORMAL,
        )

        new_nodes = split_nodes_images([no_images])

        self.assertEqual(new_nodes[0].text, "This is text with no images")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL.value)
        
        no_alt_text = TextNode(
            "This is text with an image ![](https://www.boot.dev)",
            TextType.NORMAL,
        )

        new_nodes = split_nodes_images([no_alt_text])

        self.assertEqual(new_nodes[0].text, "This is text with an image !")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL.value)

        self.assertEqual(new_nodes[1].text, "")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK.value)
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev")


if __name__ == "__main__":
    unittest.main()