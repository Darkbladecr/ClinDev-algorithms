"""Returns the first repeated item from an array if any."""


def repeatedItem(array):
    """Return first repeated item from an array if any."""
    uSet = set()
    for item in array:
        if item in uSet:
            return item
        else:
            uSet.add(item)
    raise ValueError("No item repetition")
