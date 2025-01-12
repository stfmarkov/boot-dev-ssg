from src.functions.extract_title import extract_title
from src.functions.markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    
    content = open(f"content/{from_path}", 'r').read()
    title = extract_title(content)

    template = open(template_path, 'r').read()

    content_html = markdown_to_html_node(content).replace('<html>', '').replace('</html>', '')

    print(template.replace("{{ Title }}", title).replace("{{ Content }}", content_html))