import os

from transformers.markdown_to_html_node import markdown_to_html_node
from generate.extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):


    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path, "r")
    markdown_content = markdown_file.read()

    template_file = open(template_path, "r")
    template_content = template_file.read()

    node= markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)

    new_content = template_content
    new_content = new_content.replace("{{ Title }}", title)
    new_content = new_content.replace("{{ Content }}", html)
    new_content = new_content.replace('href="/', f'href="{basepath}')
    new_content = new_content.replace('src="/', f'src="{basepath}')

    if os.path.isfile(dest_path):
        with open(dest_path, "w") as file:
            file.write(new_content)
    else:
        file = open(dest_path, "x")
        file.write(new_content)


def generate_pages_recursive(source,template, dest, basepath):
    content_dir = os.listdir(source)
    for f in content_dir:
        if os.path.isfile(f"{source}/{f}"):
            if f[-3:] == ".md":
                generate_page(f"{source}/{f}", template, f"{dest}/{f[:-3]}.html", basepath)

        else:
            if f not in os.listdir(dest):
                os.mkdir(f"{dest}/{f}")
            generate_pages_recursive(source+f"/{f}", template,  dest+f"/{f}", basepath)
