from functions.split_nodes_link import split_nodes_link
from functions.split_nodes_images import split_nodes_images
from classes.text_node import TextNode, TextType

def main():
    
    node_with_links = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.NORMAL,
    )
    new_nodes = split_nodes_link([node_with_links])

    print(new_nodes)

    node_with_images = TextNode(
        "This is text with an image ![alt text](https://www.boot.dev/image.png)",
        TextType.NORMAL,
    )

    new_nodes = split_nodes_images([node_with_images])

    print(new_nodes)

main()