"""
Write a program that displays the "Seven Times Table". That is, the result of
multiplying 7 by every number from 0 to 12 inclusive. The output might start:
0 x 7 = 0
1 x 7 = 7
2 x 7 = 14
and so on.
"""

number = 7
for count in range(0, 13):
    print(number, 'x', count, '=', number * count)

exit(0)
