def shop():
    print("""
BPP Pizza Price Calculator
==========================""")
    while True:
        total_pizza = (input("Please enter how many pizzas required: \n"))
        if str.isdigit(total_pizza):
            total_pizza = int(total_pizza)
        else:
            print("Please enter a number.")
            continue

        if total_pizza < 1:
            print("please enter a number greater than 0.")
            continue
        else:
            break

    pizza_price = 12.00
    total_price = total_pizza * pizza_price

    while True:
        day_of_week = input("Is it a Tuesday? (y or n) \n").lower()
        if day_of_week == "y":
            total_price = total_price - (total_price * 50/100)
            total_price = round(total_price,2)
            break
        elif day_of_week == "n":
            break
        else:
            print("Please enter a valid input.")
            continue

    while True:
        delivery = input("Is this order for delivery? (y or n) \n").lower()
        if delivery == "y":
            if total_pizza >= 5:
                break
            else:
                total_price = total_price + 2.50
                total_price = round(total_price, 2)
                break

        elif delivery == "n":
                break
        else:
            print("Please enter a valid input.")
            continue

    while True:
        app_user = input("Is this order via the new BPP app? (y or n) \n").lower()
        if app_user == "y":
            total_price = total_price - (total_price * 25/100)
            total_price = format(round(total_price, 2),".2f")
            break
        elif app_user == "n":
            total_price = format(round(total_price, 2), ".2f")
            break
        else:
            print("Please enter a valid input.")
            continue
    print(f"Total price: £{total_price}")

shop()