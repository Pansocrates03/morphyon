# Morphyon

Morphyon is a frontend framework made in python made for you to bee able to create webpages using only Python language

Example usage
```py
# Import Master Class
from src.morphyon import Morphyon

# Import Components
from src.morphyon.components import Button, Component, Header, Input, ListC

# Import Other Objects
from src.morphyon.attributes import Attributes
from src.morphyon.styles import Style

# Create an empty Component
myComponent = Component(
    style=Style({"color": "red"}),
    content="This Is My Content"
)

myButton = Button("Click me")

# Start the app
app = Morphyon()

# Add components
app.addComponent(Header("This  is my header"))
app.addComponent(myComponent)
app.addComponent(Input("hfdius","jdfks"))
app.addComponent(ListC(True, ["1", "dsaas", "dfjk"]))
app.addComponent(myButton)

# Build the app
app.build()

# Host the app
#app.listen(port=8000)
```