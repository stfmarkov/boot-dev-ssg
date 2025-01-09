import unittest

from src.functions.split_nodes_link import split_nodes_link
from src.classes.text_node import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):
    def test_eq(self):

        base_case = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([base_case])

        self.assertEqual(new_nodes[0].text, "This is text with a link ")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL.value)

        self.assertEqual(new_nodes[1].text, "to boot dev")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK.value)
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev")

        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[2].text_type, TextType.NORMAL.value)

        self.assertEqual(new_nodes[3].text, "to youtube")
        self.assertEqual(new_nodes[3].text_type, TextType.LINK.value)
        self.assertEqual(new_nodes[3].url, "https://www.youtube.com/@bootdotdev")

        no_links = TextNode(
            "This is text with no links",
            TextType.NORMAL,
        )

        new_nodes = split_nodes_link([no_links])

        self.assertEqual(new_nodes[0].text, "This is text with no links")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL.value)

        no_anchor_text = TextNode(
            "This is text with a link [](https://www.boot.dev)",
            TextType.NORMAL,
        )

        new_nodes = split_nodes_link([no_anchor_text])

        self.assertEqual(new_nodes[0].text, "This is text with a link ")
        self.assertEqual(new_nodes[0].text_type, TextType.NORMAL.value)

        self.assertEqual(new_nodes[1].text, "")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK.value)
        self.assertEqual(new_nodes[1].url, "https://www.boot.dev")


if __name__ == "__main__":
    unittest.main()