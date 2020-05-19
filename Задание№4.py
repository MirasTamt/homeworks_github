# <<<<<<< Homework#3
# # 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# # Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# # При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# # Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# # Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
# import math

# def my_func_easy(x,y):
#     if y % 2 == 0:
#         result = x**(y*(-1))
#         print(result)
#     else:
#         result = x**(y*(-1))
#         print(int(result)*(-1))

# def my_function_hard(x,y):
#     new_list =[]
#     if y>0 or y%2==0:
#         while len(new_list)!= abs(y):
#             new_list.append(x)
#         for i in range(1,len(new_list)):
#             new_list[i]=new_list[i-1]*new_list[i]
#         print(new_list[i])
#     else:
#         while len(new_list)!= abs(y):
#             new_list.append(x)
#         for i in range(1,len(new_list)):
#             new_list[i]=new_list[i-1]*new_list[i]
#         print(new_list[i]*(-1))


# my_func_easy(int(input('x = ')),int(input('y = '))*(-1))
# my_function_hard(int(input('x = ')),int(input('y = '))*(-1))
# =======
# # 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

# user_number = str(input("Введите число: "))
# while len(user_number)>1:
#     max_digit = max(sorted(user_number))
#     print(f"Наибольшая цифра в числе : {max_digit}")
#     break
# else: print(f"Наибольшая цифра в числе : {user_number}")
# >>>>>>> master
