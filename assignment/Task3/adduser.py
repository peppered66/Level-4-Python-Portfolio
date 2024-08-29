if __name__ == "__main__":
    import password_module as p
    known_usernames = p.grab_usernames()
    entry_string = ""
    while True:
        user_input = input("Please enter a username: ").lower()
        matches = 0
        for user in known_usernames:
            username = user.split(":")[0]
            if user_input == username:
                matches += 1
            else:
                continue

        if matches > 0:
            print("Username already exists.")
            continue
        else:
            real_name = p.real_name()
            password = p.create_password()
            entry_string = f"{user_input}:{real_name}:{password}\n"

        with open('password.txt', 'a') as f:
            print("New user created.")
            f.write(entry_string)
            exit()

