if __name__ == "__main__":
    import password_module as p
    known_users = p.grab_entries()
    while True:
        user_input = input("Please enter a username: ").lower()
        matches = 0
        for user in known_users:
            username = user.split(":")[0]
            if user_input == username:
                matches += 1
            else:
                continue

        if matches == 0:
            print("Username was not found.")
            continue
        else:
            break

    index = 0
    for user in known_users:
        username = user.split(":")[0]
        if user_input == username:
            break
        else:
            index += 1

    existing_username = known_users[index].split(":")[0]
    existing_name = known_users[index].split(":")[1]
    existing_hash = known_users[index].split(":")[2].replace("\n", "")
    while True:
        user_pass = p.check_password()
        if user_pass == existing_hash:
            print("Access granted.")
            break
        else:
            print("Incorrect password.")
            continue