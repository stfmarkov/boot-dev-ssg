import re

def extract_markdown_images(text):
    pattern = r'!\[(.*?)\]\((.*?)\)'
    images = re.findall(pattern, text)
    return images