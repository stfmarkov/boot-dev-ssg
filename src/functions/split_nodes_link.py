from src.functions.extract_markdown_links import extract_markdown_links
from src.classes.text_node import TextNode, TextType

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        node_text = node.text
        md_links = extract_markdown_links(node_text)

        if len(md_links) == 0:
            new_nodes.append(TextNode(node_text, TextType.NORMAL))
            continue

        for md_link in md_links:

            if(len(md_link) == 0):
                continue
            
            text_before_link = node_text.split(f"[{md_link[0]}]")[0]

            new_nodes.append(TextNode(text_before_link, TextType.NORMAL))
            new_nodes.append(TextNode(md_link[0], TextType.LINK, md_link[1]))

            node_text = node_text.replace(f"[{md_link[0]}]({md_link[1]})", '')
            node_text = node_text.replace(f"{text_before_link}", '')

        new_nodes.append(TextNode(node_text, TextType.NORMAL))

    return new_nodes