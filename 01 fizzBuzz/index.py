"""FizzBuzz Program.

Write a program that prints the integers from 1 to 100 (inclusive).
- for multiples of three, print Lub (instead of the number)
- for multiples of five, print Dub (instead of the number)
- for multiples of both three and five, print LubDub (instead of the number)
"""
for i in xrange(100):
    isLub = i % 3 == 0
    isDub = i % 5 == 0
    if isLub and isDub:
        result = 'LubDub'
    elif isLub:
        result = 'Lub'
    elif isDub:
        result = 'Dub'
    else:
        result = i
    print(result)
