from .base import Component
from ..styles import Style
from ..utils.helpers import createUniqueId

class Button(Component):

    def __init__(self, content=None):
        defaultStyle = (
            Style()
            .set_property("background_color", "blue")
            .set_property("color", "white")
            .set_property("border_radius", "5px")
            .set_property("padding", "10px 20px")
            .set_property("border", "none")
            .set_property("cursor", "pointer")
        ) 
        super().__init__(content)
        self.tag = "button"
        self.style = defaultStyle

    def render(self) -> tuple[str, str]:
        # Call the parent class's render method
        return super().render()