"""Stack implementation.

A stack is an abstract data type that stores a collection of elements, with two principal operations:
* push: adds an element to the collection
* pop: removes the most recently added element that was not yet removed.
The order in which elements are poped is `Last In First Out` aka. `LIFO`.
"""


class Stack:
    """Stack class."""

    def __init__(self):
        """Initialize class with blank list of data."""
        self.data = list()

    def push(self, item):
        """Add the item in 0(1)."""
        self.data.append(item)

    def pop(self):
        """Pop the last inserted item in O(1); if there are no more items it returns `undefined`."""
        return self.data.pop()

    def size(self):
        """Return the number of elements in the stack in O(1)."""
        return len(self.data)
