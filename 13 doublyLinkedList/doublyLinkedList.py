"""Doubly Linked List."""


class DoublyLinkedList:
    """Doubly Linked List class."""

    def __init__(self):
        """Initialize data."""
        self.head = None
        self.tail = None

    def add(self, value):
        """Add an item in O(1)."""
        node = {'value': value, 'next': None, 'prev': None}
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail['next'] = node
            node['prev'] = self.tail
        self.tail = node

    def dequeue(self):
        """FIFO removal in O(1)."""
        if self.head is not None:
            value = self.head['value']
            self.head = self.head['next']
            if self.head is None:
                self.tail = None
            else:
                self.head['prev'] = None
            return value

    def pop(self):
        """LIFO removal in O(1)."""
        value = self.tail['value']
        self.tail = self.tail['prev']
        if self.tail is None:
            self.head = None
        else:
            self.tail['next'] = None
        return value

    def values(self):
        """Return an iterator over the values."""
        current = self.head
        values = list()
        while current:
            if current['value'] is not None:
                values.append(current['value'])
            current = current['next']
        return values
