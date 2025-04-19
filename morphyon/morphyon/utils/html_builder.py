import os

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Document</title> 
</head>
<body>
    {slot}
</body>
</html>
"""

def builder(components):

    # Check if the components are valid
    if not all(hasattr(x, "render") and callable(x.render) for x in components):
        raise ValueError("Todos los elementos en 'content' deben tener un método 'render'")
    
    # Create the build directory if it doesn't exist
    os.makedirs("build", exist_ok=True)

    # Create the content by rendering each component
    html_content = "".join([x.render()[0] for x in components])
    with open("build/index.html", "w") as f:
        f.write(HTML_TEMPLATE.format(slot=html_content))
    f.close()

    # Create the CSS by rendering each component's style
    css_content = "".join([x.render()[1] for x in components])
    with open("build/style.css", "w") as f:
        f.write(css_content)
    f.close()