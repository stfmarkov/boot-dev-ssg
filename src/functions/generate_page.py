from src.functions.extract_title import extract_title
from src.functions.markdown_to_html_node import markdown_to_html_node
from os.path import exists
from os import makedirs

def generate_page(from_path, template_path, dest_path):

    def create_directory(path):
        if not exists(path):
            makedirs(path)

    def write_file(path, content):
        with open(path, 'w') as file:
            file.write(content)

    
    
    content = open(f"content/{from_path}", 'r').read()
    title = extract_title(content)

    template = open(template_path, 'r').read()

    content_html = markdown_to_html_node(content).replace('<html>', '').replace('</html>', '')

    page_content = template.replace("{{ Title }}", title).replace("{{ Content }}", content_html)


    directory_structure = '/'.join(dest_path.split('/')[:-1])
    
    create_directory(f"public/{directory_structure}")

    write_file(f"public/{dest_path}", page_content)

    