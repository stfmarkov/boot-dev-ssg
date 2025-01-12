import re

def markdown_to_blocks(markdown):
    blocks = re.split(r'\n\s*\n', markdown)

    white_space_removed = list(map(lambda block: block.strip(), blocks))
    empty_removed = list(filter(lambda block: block != '' and block !='\n', white_space_removed))

    return empty_removed