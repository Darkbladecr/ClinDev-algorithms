"""Returns a random int with randomInt Func."""
import math
import random


def randomInt(start, before):
    """Return a random int between start and before."""
    return start + int(math.floor(random.random() * (before - start)))
