from math import factorial

def fact(n):
    for num in range(1, n + 1):
        yield factorial(num)

for el in fact(int(input('Input number: '))):
    print(el)
