# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.y
user_number = str(input("Пожалуйста введите n: "))
print(int(user_number) + int(2*user_number) + int(3*user_number))