import random as r
characters = "abcdeifghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encryption():
    length = r.randrange(2,20)
    return"".join(r.choices(characters,k=length))

message = input("Please enter message.\n")
encrypted_message = encryption().join(message)
print(encrypted_message)

encryption()