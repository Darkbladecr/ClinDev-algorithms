"""Merge Sort."""
import math


def mergeSort(array):
    """Split step of mergeSort."""
    length = len(array)
    if length <= 1:
        return array

    middle = int(math.floor(length / 2))
    left = array[:middle]
    right = array[middle:]

    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    """Merge (conquer) step of mergeSort."""
    array = list()
    lIndex = 0
    rIndex = 0
    lLength = len(left)
    rLength = len(right)

    while lIndex + rIndex < lLength + rLength:
        lItem = left[lIndex] if lLength > lIndex else None
        rItem = right[rIndex] if rLength > rIndex else None
        if lItem is None or lItem > rItem:
            array.append(rItem)
            rIndex += 1
        elif rItem is None or lItem < rItem:
            array.append(lItem)
            lIndex += 1
    return array
