def decimal_to_binary(n):
    binary_representation = ""
    while n > 0:
        binary_representation = str(n % 2) + binary_representation
        n //= 2

    return '0b' + binary_representation

number = 10
binary_representation = decimal_to_binary(number)
print(f"The binary representation of {number} is: {binary_representation}")

decimal_to_binary(10)