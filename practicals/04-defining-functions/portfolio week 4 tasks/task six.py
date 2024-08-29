"""
Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format.
"""
def temperature():
    celsius_input = input("Please write the temperature measured in celsius. ")
    celsius_input = float(celsius_input)
    fahrenheit = celsius_input * 1.8 + 32
    print(f"This temperature converted to fahrenheit is {fahrenheit}c fahrenheit.")

temperature()