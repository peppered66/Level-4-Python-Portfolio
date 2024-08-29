"""
Over the summer, temperatures in Yorkshire reached 38.4C. Write a program that
converts this value in Celsius to the equivalent temperature in Fahrenheit, and then
displays both.
"""

celsius = 38.4
fahrenheit = celsius * 1.8 + 32

print(f"""
The weather in Leeds today is {celsius} degrees celsius.
This could also be measured in fahrenheit in which the temperature would be {fahrenheit} degrees.
""")


celsius_input = float(input("Please write the temperate today in celsius. "))
fahrenheit = celsius_input * 1.8 + 32

print(f"""
The weather in Leeds today is {celsius_input} degrees celsius. This could also be
measured in fahrenheit in which the temperature would be {fahrenheit} degrees fahrenheit.
""")