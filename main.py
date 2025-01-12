from src.functions.static_to_public import static_to_public	
from src.functions.generate_pages_recursively import generate_pages_recursively

def main():
    static_to_public()
    generate_pages_recursively('content', 'template.html', 'public')
main()