import os
from generate.copy_directory import copy_directory
from generate.generate_page import generate_page


def main():

    copy_directory("static", "public")
    generate_pages_in_directory("content", "public")


def generate_pages_in_directory(source, dest):
    content_dir = os.listdir(source)
    for f in content_dir:
        if os.path.isfile(f"{source}/{f}"):
            if f[-3:] == ".md":
                generate_page(f"{source}/{f}", "template.html", f"{dest}/{f[:-3]}.html")

        else:
            if f not in os.listdir(dest):
                os.mkdir(f"{dest}/{f}")
            generate_pages_in_directory(source+f"/{f}", dest+f"/{f}")
main()
