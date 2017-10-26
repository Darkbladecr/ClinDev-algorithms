"""Binary Search."""
import math


def binarySearch(array, element, start=0, end=None):
    """Search for specific element in a given sorted array.

    @returns the index of the element (-1 if its not found)
    """
    if end is None:
        end = len(array) - 1
    if end < start:
        return -1
    middle = int(math.floor((start + end) / 2))
    if element == array[middle]:
        return middle
    elif element < array[middle]:
        return binarySearch(array, element, start, middle - 1)
    else:
        return binarySearch(array, element, middle + 1, end)
