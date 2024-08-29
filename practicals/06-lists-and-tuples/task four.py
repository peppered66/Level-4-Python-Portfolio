def encryption(x):
    message = []
    y =x[::-1]
    c = y.replace(" ", "")
    message.append(c)
    print(message)

encryption("train")