"""Testing for anagram."""


def areAnagrams(s1, s2):
    """Given two strings determines if they are anagrams of each other."""
    charCount = dict()
    for char in s1:
        charCount[char] = (charCount[char] if char in charCount else 0) + 1
    for char in s2:
        if char not in charCount:
            return False
        charCount[char] = charCount[char] - 1
    return sum(charCount.values()) == 0
