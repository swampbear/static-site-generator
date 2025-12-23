from generate.copy_directory import copy_directory
from generate.generate_page import generate_pages_in_directory


def main():

    copy_directory("static", "public")
    generate_pages_in_directory("content", "public")


main()
