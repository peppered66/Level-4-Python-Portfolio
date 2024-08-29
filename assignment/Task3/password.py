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
            new_password_hash = p.create_password()
            known_users.pop(index)
            entry_string = f"{existing_username}:{existing_name}:{new_password_hash}\n"
            known_users.insert(index, entry_string)
            with open('password.txt', 'w') as f:
                for user in known_users:
                    f.write(user)
                print("Password updated.")
                break
        else:
            print("Error passwords not matching.")
            continue











