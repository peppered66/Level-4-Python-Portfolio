"""
Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae).
"""

def convertcelsius():
    celsius_input = float(input("Please write the temperate today measured in celsius. "))
    fahrenheit = celsius_input * 1.8 + 32
    print(f"Today's temperature is {celsius_input} degrees celsius, which converts to {fahrenheit} degrees fahrenheit.")

def convertfahrenheit():
    fahrenheit_input = float(input("Please write the temperature today measured in fahrenheit. "))
    celsius = ((fahrenheit_input-32)*5)/9
    print(f"Today's temperature is {fahrenheit_input} degrees fahrenheit, which converts to {celsius} degrees celsius.")


convertcelsius()

convertfahrenheit()
