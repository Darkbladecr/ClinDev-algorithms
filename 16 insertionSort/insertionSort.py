"""Insertion Sort."""


def insertionSort(array):
    """Sort an array using insertion sort."""
    array = list(array)
    for i in xrange(len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array
