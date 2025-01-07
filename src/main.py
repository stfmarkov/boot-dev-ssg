from text_node import TextNode, TextType

def main():
    text_node = TextNode('This is a text node', TextType.BOLD, 'https://www.example.com')
    
    print(text_node)

main()