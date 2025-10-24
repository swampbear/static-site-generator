import re

# Regex for links (\w+:\/\/)(\w+).(\w+\.\w+\/)(\w+\.\w+) returns https://i.imgur.com/fJRm4Vk.jpeg

## Regex for images (\[).+?(\]) returns ![words inside]


def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"[^!]\[(.*?)\]+\((.*?)\)", text)
    return matches
