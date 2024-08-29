"""
Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit, like so:
Enter a temperature in Celsius: 32.5
32.5C is equivalent to 90.5F.
"""

celsius_input = input("Please write the temperate today measured in celsius. ")
celsius_input = float(celsius_input)
fahrenheit = celsius_input * 1.8 + 32

print(f"""
The weather in celsius is {celsius_input} degrees. This converted to fahrenheit would be {fahrenheit} degrees.
""")

exit(0)