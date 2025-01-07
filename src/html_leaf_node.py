from htmlnode import HTMLNode

class HTMLLeafNode(HTMLNode):
    def __init__(self, tag, value, props = None, ):
        super().__init__(tag, value, props=props)


    def to_html(self):
        if(self.value == None):
            raise ValueError('Value cannot be None')
        if(self.tag == None):
            return self.value
        
        props = self.props_to_html()

        if props:
            props = ' ' + props

        return f'<{self.tag}{props}>{self.value}</{self.tag}>'
    