"""Shuffle an input array."""
import random


def shuffle(array):
    """Shuffle items in an array."""
    array = list(array)
    length = len(array)
    for i in xrange(length):
        randomChoiceIndex = random.randint(i, length - 1)
        array[i], array[randomChoiceIndex] = array[randomChoiceIndex], array[i]
    return array
