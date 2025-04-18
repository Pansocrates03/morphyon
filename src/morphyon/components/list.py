from .base import Component
from ..styles import Style
from typing import List  # Corrige el import de List

class ListC(Component):
    def __init__(self, isOrdered: bool = False, items: List[str] = []):
        super().__init__()
        if isOrdered:
            self.tag = "ol"
        else:
            self.tag = "ul"
        self.content = []  # Inicializa como una lista vacía

        for item in items:
            self.content.append(Component(  # Solo llama a append
                tag="li",
                content=item
            ))