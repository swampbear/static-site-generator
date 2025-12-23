import sys
from generate.generate_page import generate_pages_recursive
from generate.copy_directory import copy_directory


def main():
    args = sys.argv
    base_path = ""
    if len(args) == 2:
        base_path = sys.argv[1]+base_path
    elif len(args)>2:
        raise ValueError("Too many arguments")

    static_path = "static"
    docs_path = "docs"
    copy_directory(static_path, docs_path)

    generate_pages_recursive("content", "template.html",  docs_path, base_path)


main()
