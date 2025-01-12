from src.functions.markdown_to_blocks import markdown_to_blocks
from src.functions.block_to_block_type import block_to_block_type

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)

        if(block_type == 'heading' and block[1] != '#'):
            return block[1:].strip()
        
    raise Exception("No title found")

