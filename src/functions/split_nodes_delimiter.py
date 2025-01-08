from src.classes.text_node import TextNode, TextType
from enum import Enum
import re


class DelimiterType(Enum):
    BOLD = '**'
    ITALIC = '*'
    CODE = '`'

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_nodes = []

    def check_inner_tag(text, delimiter, full_text):
        escaped_delimiter = re.escape(delimiter)
        pattern = rf"{escaped_delimiter}{re.escape(text)}{escaped_delimiter}"
        match = re.search(pattern, full_text)
    
        return match is not None 

    if delimiter not in [item.value for item in DelimiterType]:
        raise ValueError('Invalid delimiter')

    for node in old_nodes:
        if delimiter in node.text:
            text_parts = node.text.split(delimiter)
            print(text_parts)
            for text_part in text_parts:
                type = TextType.NORMAL
                is_inner_tag = check_inner_tag(text_part, delimiter, node.text)
                if is_inner_tag:
                    type = text_type
                return_nodes.append(TextNode(text_part, type))
        else:
            return_nodes.append(node)

    return return_nodes