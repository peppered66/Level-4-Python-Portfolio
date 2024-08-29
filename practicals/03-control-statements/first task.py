"""
Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise it should print
a greeting with their name as before.
"""

user_name = input("Hello, what is your name? ")
if user_name == "":
    print(f"Hello stranger!")
    exit(0)
else:
    print(f"Hello {user_name}. Great to meet you!")
    exit(0)
