"""
Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.
"""

def string_calculator(x):
    lower_count = 0
    upper_count = 0
    for character in x:
        if character.islower():
            lower_count +=1
        else:
            if character.isupper():
                upper_count +=1

    print(f"Capital count {upper_count} lowercase count {lower_count}.")

string_calculator("Hello World.")