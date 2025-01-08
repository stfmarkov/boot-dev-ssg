import re
def extract_markdown_links(text):
    patern = r'\[(.*?)\]\((.*?)\)'
    links = re.findall(patern, text)
    return links