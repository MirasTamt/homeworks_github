# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_number = str(input("Введите число: "))
while len(user_number)>1:
    max_digit = max(sorted(user_number))
    print(f"Наибольшая цифра в числе : {max_digit}")
    break
else: print(f"Наибольшая цифра в числе : {user_number}")