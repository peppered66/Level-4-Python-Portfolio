"""
Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.
"""
def password_creator():
    while True:
        password = input("Please input new password. ")
        if len(password) < 8:
            print("Error 8 characters minimum.")
            continue
        elif len(password) > 12:
            print("Error 12 characters maximum.")
            continue
        password_confirmation = input("Please confirm new password (re-enter same password). ")

        if password == password_confirmation:
            print("Password accepted and set.")
            break

        else:
            print("Passwords not matching, please try again.")
            continue

password_creator()