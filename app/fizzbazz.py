for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBazz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Bazz')
    else:
        print(n)