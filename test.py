from src.morphyon import Morphyon
from src.morphyon.components import Button, Component, Header, Input, ListC
from src.morphyon.attributes import Attributes
from src.morphyon.styles import Style

myComponent = Component(
    style=Style({"color": "red"}),
    content="This Is My Content"
)

mybutton = Button(
    content="click me"
)

myList = ListC(isOrdered=False, items=["One", "Two", "Three"])

app = Morphyon()
app.addComponent(mybutton)
app.addComponent(mybutton)
app.addComponent(myList)
app.build()
app.listen(port=8000)