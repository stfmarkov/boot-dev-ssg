from src.functions.extract_markdown_images import extract_markdown_images
from src.classes.text_node import TextNode, TextType

def split_nodes_images(old_nodes):
    new_nodes = []

    for node in old_nodes:
        node_text = node.text
        md_images = extract_markdown_images(node_text)

        if len(md_images) == 0:
            new_nodes.append(TextNode(node_text, node.text_type, node.url))
            continue

        for md_image in md_images:

            if(len(md_image) == 0):
                continue
            
            text_before_link = node_text.split(f"![{md_image[0]}]")[0]

            new_nodes.append(TextNode(text_before_link, node.text_type, node.url))
            new_nodes.append(TextNode(md_image[0], TextType.IMAGE.value, md_image[1]))

            node_text = node_text.replace(f"![{md_image[0]}]({md_image[1]})", '')
            node_text = node_text.replace(f"{text_before_link}", '')

        new_nodes.append(TextNode(node_text, node.text_type, node.url))

    return new_nodes