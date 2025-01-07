from text_node import TextNode, TextType
from functions.split_nodes_delimiter import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", TextType.NORMAL)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    print(new_nodes)

main()