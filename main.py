from src.functions.static_to_public import static_to_public	
from src.functions.generate_page import generate_page

def main():
    static_to_public()
    generate_page('index.md', 'template.html', 'index.html')
main()