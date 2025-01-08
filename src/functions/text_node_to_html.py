from src.classes.text_node import TextType
from src.classes.html_leaf_node import HTMLLeafNode

def text_node_to_html(text_node):
    print(text_node)

    if(text_node.text_type == TextType.NORMAL.value):
        return HTMLLeafNode(None, text_node.text)
    elif(text_node.text_type == TextType.BOLD.value):
        return HTMLLeafNode('b', text_node.text)
    elif(text_node.text_type == TextType.ITALIC.value):
        return HTMLLeafNode('i', text_node.text)
    elif(text_node.text_type == TextType.LINK.value):
        return HTMLLeafNode('a', text_node.text, props={'href': text_node.url})
    elif(text_node.text_type == TextType.IMAGE.value):
        return HTMLLeafNode('img', None, props={'src': text_node.url})
    elif(text_node.text_type == TextType.CODE.value):
        return HTMLLeafNode('code', text_node.text)
    else:
        raise ValueError('Invalid TextType')