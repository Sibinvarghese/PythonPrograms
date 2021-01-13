def fact(num1):
    factorial = 1
    for i in range(1, (num1+1)):
        factorial = factorial * i
    print(factorial)


fact(3)
