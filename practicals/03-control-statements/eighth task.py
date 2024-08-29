"""
 Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times".
"""

number = int(input("Please enter desired number."))
limit = 12
if number < 0:
    for count in range(limit, 0, -1):
        print(number, 'x', count, '=', number * count)
else:
    for count in range(1,13):
        print(number, 'x', count, '=', number * count)

exit(0)