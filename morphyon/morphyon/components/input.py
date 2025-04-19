from .base import Component
from ..styles import Style
from ..utils.helpers import createUniqueId

class Input(Component):

    def __init__(self, type: str = "text", placeholder: str = "Placeholder"):
        super().__init__()
        self.tag = "input"
        self.class_name = createUniqueId()

    def render(self) -> tuple[str, str]:
        # Call the parent class's render method
        return super().render()