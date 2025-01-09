import unittest

from src.classes.text_node import TextNode, TextType
from src.functions.text_to_textnodes import text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        base_case_string = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        nodes = text_to_textnodes(base_case_string)
            
        self.assertEqual(nodes, [
            TextNode("This is ", TextType.NORMAL.value),
            TextNode("text", TextType.BOLD.value),
            TextNode(" with an ", TextType.NORMAL.value),
            TextNode("italic", TextType.ITALIC.value),
            TextNode(" word and a ", TextType.NORMAL.value),
            TextNode("code block", TextType.CODE.value),
            TextNode(" and an !", TextType.NORMAL.value),
            TextNode("obi wan image", TextType.IMAGE.value, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL.value),
            TextNode("link", TextType.LINK.value, "https://boot.dev")
        ])

        no_images = "This is **text** with an *italic* word and a `code block` and a [link](https://boot.dev)"

        nodes = text_to_textnodes(no_images)

        self.assertEqual(nodes, [
            TextNode("This is ", TextType.NORMAL.value),
            TextNode("text", TextType.BOLD.value),
            TextNode(" with an ", TextType.NORMAL.value),
            TextNode("italic", TextType.ITALIC.value),
            TextNode(" word and a ", TextType.NORMAL.value),
            TextNode("code block", TextType.CODE.value),
            TextNode(" and a ", TextType.NORMAL.value),
            TextNode("link", TextType.LINK.value, "https://boot.dev")
        ])

        no_links = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"

        nodes = text_to_textnodes(no_links)

        self.assertEqual(nodes, [
            TextNode("This is ", TextType.NORMAL.value),
            TextNode("text", TextType.BOLD.value),
            TextNode(" with an ", TextType.NORMAL.value),
            TextNode("italic", TextType.ITALIC.value),
            TextNode(" word and a ", TextType.NORMAL.value),
            TextNode("code block", TextType.CODE.value),
            TextNode(" and an !", TextType.NORMAL.value),
            TextNode("obi wan image", TextType.IMAGE.value, "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

        no_code = "This is **text** with an *italic* word and a [link](https://boot.dev) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        nodes = text_to_textnodes(no_code)

        self.assertEqual(nodes, [
            TextNode("This is ", TextType.NORMAL.value),
            TextNode("text", TextType.BOLD.value),
            TextNode(" with an ", TextType.NORMAL.value),
            TextNode("italic", TextType.ITALIC.value),
            TextNode(" word and a ", TextType.NORMAL.value),
            TextNode("link", TextType.LINK.value, "https://boot.dev"),
            TextNode(" and an !", TextType.NORMAL.value),
            TextNode("obi wan image", TextType.IMAGE.value, "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

if __name__ == "__main__":
    unittest.main()