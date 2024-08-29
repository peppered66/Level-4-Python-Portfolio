if __name__ == "__main__":
    import password_module as p
    existing_users = p.grab_entries()

    delete_user = input("Enter username of account you wish to remove: ")

    matches = 0
    for user in existing_users:
        username = user.split(':')[0]
        if delete_user == username:
            matches += 1
        else:
            continue

    if matches == 0:
        print("Username not found.")
        exit()

    index = 0
    for user in existing_users:
        username = user.split(":")[0]
        if delete_user == username:
            existing_users.pop(index)
            break
        else:
            index += 1
    
    with open("password.txt", 'w') as f:
        for user in existing_users:
            f.write(user)
        exit()






