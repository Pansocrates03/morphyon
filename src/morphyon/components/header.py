from .base import Component
from ..styles import Style
from ..utils.helpers import createUniqueId


class Header(Component):
    def __init__(self, content=None):
        defaultStyle = (
            Style()
            .set_property("font_size", "2em")
            .set_property("color", "black")
        ) 
        super().__init__(content)
        self.tag = "h1"
        self.class_name = createUniqueId()
        self.style = defaultStyle

    def render(self) -> tuple[str, str]:
        # Call the parent class's render method
        return super().render()

