"""Palindrome Solver."""


def isPalindrome(string):
    """Return true if the string is a palindrome."""
    reversed = string[::-1]
    return reversed == string


def isAnyPermutationPalindrome(string):
    """Return true if ANY permutation of the string is a palindrome."""
    unmatched = set()
    for char in string:
        if char in unmatched:
            unmatched.remove(char)
        else:
            unmatched.add(char)
    return len(unmatched) <= 1
