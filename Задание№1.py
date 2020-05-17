def division(x,y):
    return x/y
user_number1 = int(input('Enter x: '))
user_number2 = int(input('Enter y: '))
try:
    print(division(user_number1,user_number2))
except ZeroDivisionError:
    print('На ноль делить нельзя')
