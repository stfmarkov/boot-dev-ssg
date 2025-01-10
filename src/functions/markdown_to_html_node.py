from src.functions.markdown_to_blocks import markdown_to_blocks
from src.functions.block_to_block_type import block_to_block_type
from src.functions.text_to_textnodes import text_to_textnodes
from src.classes.html_parent_node import HTMLParentNode

def handle_heading(block):
    level = 0
    while block[level] == '#':
        level += 1

    return f'h{level}', block[level:].strip()

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)

    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if(block_type == 'heading'):
            tag, text = handle_heading(block)
            block_node = HTMLParentNode(tag, text_to_textnodes(text))

        if(block_type == 'paragraph'):
            block_node = HTMLParentNode('p', text_to_textnodes(block))

        if(block_type == 'unordered_list'):
            block_node = HTMLParentNode('ul', text_to_textnodes(block))

        if(block_type == 'ordered_list'):
            block_node = HTMLParentNode('ol', text_to_textnodes(block))

        if(block_type == 'list_item'):
            block_node = HTMLParentNode('li', text_to_textnodes(block))

        if(block_type == 'code_block'):
            block_node = HTMLParentNode('pre', text_to_textnodes(block))

        if(block_type == 'quote'):
            block_node = HTMLParentNode('blockquote', text_to_textnodes(block))

        block_nodes.append(block_node)
        

    print(block_nodes)