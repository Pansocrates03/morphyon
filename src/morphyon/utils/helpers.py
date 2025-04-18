def createUniqueId():
    # Generate a unique ID (for demonstration purposes, this is a simple counter)
    if not hasattr(createUniqueId, "counter"):
        createUniqueId.counter = 0  # Initialize the counter
    createUniqueId.counter += 1
    return f"unique_id_{createUniqueId.counter}"