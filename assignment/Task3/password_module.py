import hashlib
def create_password():
    while True:
        password = input("Please input new password. ")
        if len(password) < 8:
            print("Error 8 characters minimum.")
            continue

        elif len(password) > 12:
            print("Error 12 characters maximum.")
            continue

        password_confirmation = input("Please confirm new password (re-enter same password). ")
        if password != password_confirmation:
            print("Error passwords not matching.")
            continue
        else:
            password = hashlib.md5(password.encode()).hexdigest()
            print("Passwords matching, password set.")
            return password

def check_password():
    while True:
        password = input("Please input current password. ")
        password = hashlib.md5(password.encode()).hexdigest()
        return password

def real_name():
    while True:
        real_name = input("Please enter your real name: ")
        if any(char.isdigit() for char in real_name):
            print("Please enter characters only.")
            continue
        else:
            return real_name

def grab_usernames():
    existing_usernames = []
    with open('password.txt', 'r') as f:
        for line in f:
            existing_usernames.append(line.split(':')[0])
    return existing_usernames

def grab_entries():
    existing_users = []
    with open("password.txt", 'r') as f:
        for line in f:
            existing_users.append(line)
    return existing_users