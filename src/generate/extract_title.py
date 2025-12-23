
def extract_title(markdown):

    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            header = line.split(" ",1)[1]
            header = header.strip(" ")
            return header

    raise Exception("no h1 title")
