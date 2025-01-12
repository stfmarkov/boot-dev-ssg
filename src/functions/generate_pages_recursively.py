from os import listdir
from os.path import isdir, isfile, join
from src.functions.generate_page import generate_page

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    print(f"Generating pages recursively from {dir_path_content} with template {template_path} to {dest_dir_path}")

    content_elements = listdir(dir_path_content)

    for element in content_elements:
        element_path = join(dir_path_content, element)

        print(f"Element path: {element_path}")

        if isfile(element_path):      
            generate_page(element_path, template_path, join(dest_dir_path, element.replace('.md', '.html')))
        elif isdir(element_path):
            generate_pages_recursively(element_path, template_path, join(dest_dir_path, element))

