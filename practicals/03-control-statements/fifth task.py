"""
Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.
"""


bad_passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
def password_creator():
    while True:
        password = input("Please input new password. ")
        if len(password) < 8:
            print("Error 8 characters minimum.")
            continue

        elif len(password) > 12:
            print("Error 12 characters maximum.")
            continue

        elif password in bad_passwords:
            print("Error common password detected.")
            continue

        password_confirmation = input("Please confirm new password (re-enter same password). ")
        if password == password_confirmation:
            print("Password accepted and set.")
            break

        else:
            print("Passwords not matching, please try again.")
            continue

password_creator()




