from src.classes.htmlnode import HTMLNode

class HTMLLeafNode(HTMLNode):
    self_closing_tags = ['img', 'br', 'hr']

    def __init__(self, tag, value, props = None, ):
        super().__init__(tag, value, props=props)


    def to_html(self):
        if(self.value == None and self.tag != 'img'):
            raise ValueError('Value cannot be None')
        if(self.tag == None):
            return self.value
        
        props = self.props_to_html()

        if props:
            props = ' ' + props

        if self.tag in self.self_closing_tags:
            return f'<{self.tag}{props}/>'

        return f'<{self.tag}{props}>{self.value}</{self.tag}>'
    