import unittest

from src.functions.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_eq(self):
        

        base_case = """# This is a heading. It has some **bold** and *italic* words inside of it.

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is **the first** list item in a list block\n* This is a list item\n* This is another list item\n\n

            1. This is *the first* list item in a list block\n2. This is a list item\n3. This is another list item\n\n

            This is a text with a [link](https://www.example.com)

            This is a text with an ![image](https://www.example.com/image.jpg)

            This is a text with a [link](https://www.example.com) and an ![image](https://www.example.com/image.jpg)

            
            ```
            def test():
                return 'test'
            ```

            > This is a quote block. It has some **bold** and *italic* words inside of it.


            """
        
        html = markdown_to_html_node(base_case)  

        heading = "<h1>This is a heading. It has some <b>bold</b> and <i>italic</i> words inside of it.</h1>"
        paragraph = "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>"
        list_item = "<li>This is <b>the first</b> list item in a list block</li>"
        ordered_list_item = "<li>This is <i>the first</i> list item in a list block</li>"
        ol_tag = "<ol>"
        ul_tag = "<ul>"
        paragraph_with_link = '<p>This is a text with a <a href="https://www.example.com">link</a></p>'
        paragraph_with_image = '<p>This is a text with an <img src="https://www.example.com/image.jpg" alt="image"/></p>'
        paragraph_with_link_and_image = '<p>This is a text with a <a href="https://www.example.com">link</a> and an <img src="https://www.example.com/image.jpg" alt="image"/></p>'
        function_def = '<code>def test():'
        function_return = 'return \'test\'</code>'
        quote_block = "<blockquote>This is a quote block. It has some <b>bold</b> and <i>italic</i> words inside of it.</blockquote>"

        self.assertTrue(heading in html)
        self.assertTrue(paragraph in html)
        self.assertTrue(list_item in html)
        self.assertTrue(ordered_list_item in html)
        self.assertTrue(ol_tag in html)
        self.assertTrue(ul_tag in html)
        self.assertTrue(paragraph_with_link in html)
        self.assertTrue(paragraph_with_image in html)
        self.assertTrue(paragraph_with_link_and_image in html)
        self.assertTrue(function_def in html)
        self.assertTrue(function_return in html)
        self.assertTrue(quote_block in html)




if __name__ == "__main__":
    unittest.main()