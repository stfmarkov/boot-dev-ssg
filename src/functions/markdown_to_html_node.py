from src.functions.markdown_to_blocks import markdown_to_blocks
from src.functions.block_to_block_type import block_to_block_type
from src.functions.text_to_textnodes import text_to_textnodes
from src.classes.html_parent_node import HTMLParentNode
from src.classes.html_leaf_node import HTMLLeafNode
from src.functions.text_node_to_html import text_node_to_html

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
            children = text_to_textnodes(text)
            childern_html = [text_node_to_html(child) for child in children]
            block_node = HTMLParentNode(tag, childern_html)

        if(block_type == 'paragraph'):
            children = text_to_textnodes(block)
            childern_html = [text_node_to_html(child) for child in children]
            block_node = HTMLParentNode('p', childern_html)

        if(block_type == 'unordered_list'):
            children = block.split('\n')

            def to_text_node(child):
                return HTMLLeafNode('li', child[2:])

            childern_html = list(map(to_text_node, children))
            block_node = HTMLParentNode('ul', childern_html)

            
        if(block_type == 'ordered_list'):
            children = block.split('\n')

            def to_text_node(child):
                return HTMLLeafNode('li', child[3:])

            childern_html = list(map(to_text_node, children))
            block_node = HTMLParentNode('ol', childern_html)

        if(block_type == 'code'):
            block_node = HTMLLeafNode('code', block[3:-3].strip().replace('\n', '').strip())
            
        if(block_type == 'quote'):
            children = text_to_textnodes(block[1:])
            childern_html = [text_node_to_html(child) for child in children]
            block_node = HTMLParentNode('blockquote', childern_html)

        block_nodes.append(block_node)
    
    return f"<html>{''.join([node.to_html() for node in block_nodes])}</html>"