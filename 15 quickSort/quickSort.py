"""Quck Sort."""
import math
import random


def quickSort(array):
    """Sort an array using quick sort."""
    array = list(array)
    partition(array, 0, len(array))
    return array


def partition(array, begin, end):
    """Partition the (begin, end) i of the array."""
    # Terminate the recursion
    length = end - begin
    if length <= 1:
        return

    # Randomly select a pivot and move it to the head of the array
    pivot = begin + int(math.floor(random.random() * length))
    array[begin], array[pivot] = array[pivot], array[begin]
    pivot = begin

    # Loop through all the elements, partitioning around the pivot
    for i in xrange(begin + 1, end):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]

    # Partition all the elements less than the pivot
    partition(array, begin, pivot - 1)
    # Partition all the elements more than the pivot
    partition(array, pivot + 1, end)
