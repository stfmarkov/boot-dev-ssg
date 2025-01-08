from functions.extract_markdown_images import extract_markdown_images
from functions.extract_markdown_links import extract_markdown_links

def main():
    
    images_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(images_text))

    links_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(links_text))

main()