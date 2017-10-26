"""Convert a string to a integer."""


def atoi(string):
    """Convert a string to an integer."""
    zeroCode = ord('0')
    sign = 1
    if string[0] == '-':
        string = string[1:]
        sign = -1

    acc = 0
    for char in string:
        charCode = ord(char)
        if charCode == 46:
            break
        elif charCode >= 48 and charCode <= 56:
            acc = acc * 10 + (ord(char) - zeroCode)
        else:
            return float('nan')

    return sign * acc
