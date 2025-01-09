from src.functions.split_nodes_images import split_nodes_images
from src.classes.text_node import TextNode, TextType
from src.functions.split_nodes_delimiter import split_nodes_delimiter
from src.functions.split_nodes_images import split_nodes_images
from src.functions.split_nodes_link import split_nodes_link

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.NORMAL.value)

    bold_nodes_extracted = split_nodes_delimiter([text_node], '**', TextType.BOLD.value)
    italic_nodes_extracted = split_nodes_delimiter(bold_nodes_extracted, '*', TextType.ITALIC.value)
    code_nodes_extracted = split_nodes_delimiter(italic_nodes_extracted, '`', TextType.CODE.value)
    images_nodes_extracted = split_nodes_images(code_nodes_extracted)
    links_nodes_extracted = split_nodes_link(images_nodes_extracted)


    return list(filter(lambda x: x.text != '', links_nodes_extracted))