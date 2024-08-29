"""
Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error.
"""
def password_creator():
    while True:
        password = input("Please input new password. ")
        password_confirmation = input("Please confirm new password (re-enter same password). ")

        if password == password_confirmation:
            print("Password accepted and set.")
            break

        else:
            print("Passwords not matching, please try again.")


password_creator()