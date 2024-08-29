def factors(n):
    factor_list =[]
    for i in range (1, n+1):
        if n % i == 0:
            factor_list.append(i)
    print(factor_list)


factors(10)