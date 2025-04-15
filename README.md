# Py2Web

Py2web is a frontend framework made in python made for you to bee able to create webpages using only Python language

Example usage
```py
from src.py2web import Component, Style, Button, Header, build

listOfCOmponentes = [
    Header("Hello World"),
    
    Component([
        Button("Click Me"),
        Button("Click 2")
    ]).set_tag("div").set_style(Style().set_property("background_color", "green").set_property("color", "white")),
]

# Build the components into an index.html file
build(listOfCOmponentes)

print("Build completed.")
```