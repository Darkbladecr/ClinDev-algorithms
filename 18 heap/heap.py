"""Heap Data Structure."""


def compare(a, b):
    """Compare variables in size."""
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


class Heap:
    """Heap data structure.

    A heap is used as a priority queue
    Note: The default compare behavior gives you a min heap
    """

    def __init__(self):
        """Initialize data."""
        self.data = list()

    def __left(self, nodeIndex):
        """Return left value."""
        return (2 * nodeIndex) + 1

    def __right(self, nodeIndex):
        """Return right value."""
        return (2 * nodeIndex) + 2

    def __parent(self, nodeIndex):
        """Return parent index."""
        if nodeIndex % 2 == 0:
            return (nodeIndex - 2) / 2
        else:
            return (nodeIndex - 1) / 2

    def __siftUp(self, index):
        """Move the node at the given index up to its proper place in the heap."""
        parent = self.__parent(index)
        while index > 0 and compare(self.data[parent], self.data[index]) > 0:
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent
            parent = self.__parent(index)

    def __minIndex(self, left, right):
        """Return the minimum index."""
        if right >= len(self.data):
            if left >= len(self.data):
                return -1
            else:
                return left
        else:
            if compare(self.data[left], self.data[right] <= 0):
                return left
            else:
                return right

    def __siftDown(self, nodeIndex):
        """Move the node at the given index down to its proper place in the heap."""
        minNode = self.__minIndex(self.__left(nodeIndex), self.__right(nodeIndex))

        while minNode >= 0 and compare(self.data[nodeIndex], self.data[minNode] > 0):
            self.data[minNode], self.data[nodeIndex] = self.data[nodeIndex], self.data[minNode]
            nodeIndex = minNode
            minNode = self.__minIndex(self.__left(nodeIndex), self.__right(nodeIndex))

    def add(self, element):
        """Add element to heap."""
        self.data.append(element)
        self.__siftUp(len(self.data) - 1)

    def extractRoot(self):
        """Retrieve and removes the root element of this heap in O(logn)."""
        if len(self.data) > 0:
            root = self.data[0]
            last = self.data.pop()
            if len(self.data) > 0:
                self.data[0] = last
                self.__siftDown(0)
            return root

    def size(self):
        """Length of data."""
        return len(self.data)

    def peak(self):
        """Return the peak of the heap."""
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None
