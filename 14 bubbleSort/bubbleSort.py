"""BubbleSort."""


def bubbleSortConcept(array):
    """Explain the bubble sort concept."""
    array = list(array)
    length = len(array)
    for i in xrange(length):
        for j in xrange(length):
            if length > j + 1 and array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubbleSort(array):
    """Idiomatic bubble sort implementation."""
    array = list(array)
    length = len(array)
    while True:
        swapped = False
        for j in xrange(length):
            if length > j + 1 and array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array
