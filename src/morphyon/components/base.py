from ..utils.helpers import createUniqueId

from ..attributes import Attributes
from ..styles import Style




class Component:

    # Create a simple component class
    def __init__(
        self,
        content=None,
        tag: str = "div",
        attributes: Attributes = Attributes(),
        style: Style = Style()
    ):
        self.tag = tag
        self.attributes = attributes
        self.content = content
        self.style = style

        self.attributes.setAttribute('class_name', createUniqueId())
        
    
    # SETTERS
    def set_tag(self, tag: str):
        if tag not in ["a","div", "span", "button", "h1", "h2", "h3", "p", "ol", "ul", "li", "table", "tr", "td", "th", "thead", "tbody", "tfoot", "form", "input", "select", "option", "textarea", "label", "img"]:
            raise ValueError(f"Tag '{tag}' is not supported.")
        self.tag = tag
        return self
    def set_attributes(self, attr: Attributes):
        self.attributes = attr
    def set_content(self, content):
        self.content = content
    def set_style(self, style):
        self.style = style
    
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
        
        # If there is nothing to render
        if self.content is None:
            rendered_content = ""
        # If content is a string
        elif isinstance(self.content, str):
            rendered_content = self.content
        # If content is another component
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
        
        HTML_ELEMENT = f"\n<{self.tag}{self.attributes.render()}>{rendered_content}</{self.tag}>"
        
        # Add the component's own CSS if it has style
        if self.style:
            css_content += self.style.render(self.attributes.class_name)
        
        return (HTML_ELEMENT, css_content)