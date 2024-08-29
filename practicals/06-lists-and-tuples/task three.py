def primecheck(n):
    prime = False

    if n ==1:
        print("Number is not a prime number.")
    else:
        for i in range(2, n):
            if (n % i) ==0:
                prime = True
                break

        if prime is True:
            print("number is not a prime number.")
        else:
            print("number is a prime number.")

primecheck(6)