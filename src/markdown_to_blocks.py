def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = list(map(lambda x: x.strip(), blocks))
    stripped_blocks = list(map(lambda x: x.strip("\n"), stripped_blocks))
    return stripped_blocks
