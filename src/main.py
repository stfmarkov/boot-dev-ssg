from text_node import TextNode, TextType
from functions.text_node_to_html import text_node_to_html

def main():
    text_node = TextNode('This is a text node', TextType.BOLD, 'https://www.example.com')
    
    print(text_node_to_html(text_node))

main()