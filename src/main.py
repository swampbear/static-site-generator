from generate.copy_directory import copy_directory
from generate.generate_page import generate_page


def main():

    copy_directory("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()
