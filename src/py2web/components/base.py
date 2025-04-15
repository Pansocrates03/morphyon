from ..utils.helpers import createUniqueId

class Component:

    # Create a simple component class
    def __init__(self, content=None):
        self.tag = "div"
        self.id = None
        self.class_name = createUniqueId()
        self.content = content
        self.style = None
    
    # SETTERS
    def set_tag(self, tag: str):
        if tag not in ["a","div", "span", "button", "h1", "h2", "h3", "p", "ol", "ul", "li", "table", "tr", "td", "th", "thead", "tbody", "tfoot", "form", "input", "select", "option", "textarea", "label", "img"]:
            raise ValueError(f"Tag '{tag}' is not supported.")
        self.tag = tag
        return self
    
    def set_id(self, id):
        self.id = id
        return self
    def set_class(self, class_name):
        self.class_name = class_name
        return self
    def set_content(self, content):
        self.content = content
        return self
    def set_style(self, style):
        self.style = style
        return self
    
    # GETTERS
    def get_tag(self): return self.tag
    def get_id(self): return self.id
    def get_class(self): return self.class_name
    def get_content(self): return self.content
    def get_style(self): return self.style
    
    # RENDER
    def render(self) -> tuple[str, str]:
        # Process the content based on its type
        rendered_content = ""
        css_content = ""
        
        if self.content is None:
            rendered_content = ""
        elif isinstance(self.content, str):
            rendered_content = self.content
        elif isinstance(self.content, Component):
            # If content is a single component
            html, css = self.content.render()
            rendered_content = html
            css_content = css
        elif isinstance(self.content, list):
            # If content is a list of components
            for item in self.content:
                if isinstance(item, Component):
                    html, css = item.render()
                    rendered_content += html
                    css_content += css
                elif isinstance(item, str):
                    rendered_content += item
                # Ignore other types

        id_attr = f' id="{self.id}"' if self.id else ""
        class_attr = f' class="{self.class_name}"' if self.class_name else ""
        
        HTML_ELEMENT = f"\n<{self.tag}{id_attr}{class_attr}>{rendered_content}</{self.tag}>"
        
        # Add the component's own CSS if it has style
        if self.style:
            css_content += self.style.render(self.class_name)
        
        return (HTML_ELEMENT, css_content)