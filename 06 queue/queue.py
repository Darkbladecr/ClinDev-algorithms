"""Queue implementation.

A queue is an abstract data type that serves as a collection of elements,
with two principal operations: enqueue, which adds an element to the collection,
and dequeue, which removes the earliest added element. The order in which
elements are dequeued is `First In First Out` aka. `FIFO`. The term `queue`
takes it name from the real world queues e.g. "a queue at the ticket counter".
"""


class Queue:
    """Creates a Queue."""

    def __init__(self):
        """Initialize data."""
        self.data = list()
        self.nextEnqueueIndex = 0
        self.lastDequeuedIndex = 0

    def enqueue(self, item):
        """Enqueue the item in O(1)."""
        self.data.insert(self.nextEnqueueIndex, item)
        self.nextEnqueueIndex += 1

    def dequeue(self):
        """Deqeue the item in 0(1)."""
        if self.lastDequeuedIndex != self.nextEnqueueIndex:
            dequeued = self.data[self.lastDequeuedIndex]
            del self.data[self.lastDequeuedIndex]
            self.lastDequeuedIndex += 1
            return dequeued

    def size(self):
        """Return the number of elements in the queue."""
        return self.nextEnqueueIndex - self.lastDequeuedIndex
