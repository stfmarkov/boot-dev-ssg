def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')

    white_space_removed = list(map(lambda block: block.strip(), blocks))
    empty_removed = list(filter(lambda block: block != '' and block !='\n', white_space_removed))

    return empty_removed