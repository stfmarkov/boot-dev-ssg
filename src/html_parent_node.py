from htmlnode import HTMLNode

class HTMLParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if(self.tag == None):
            raise ValueError('Tag cannot be None')
        if(len(self.children) == 0):
            raise ValueError('Children cannot be None')
                
        props = self.props_to_html()
        children = ''.join([child.to_html() for child in self.children])

        if props:
            props = ' ' + props
        
        return f'<{self.tag}{props}>{children}</{self.tag}>'