# <<<<<<< Homework#3
# # 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# # При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# # Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# # Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

# my_list=[]
# special_symbol ='Q'
# numbers=str(input('Insert string of numbers with space: ')).split(' ')
# for i in numbers:
#     my_list.append(int(i))
# print(sum(my_list))
# numbers_continue=(input('Continue string of numbers with space OR for exit insert Q: ').lower()).split(' ')
# for i in numbers_continue:
#     if i != 'q':
#         my_list.append(int(i))
#     else:
#         continue
# print(sum(my_list))
# =======
# my_list = [7, 5, 3, 3, 2]
# print(type(my_list))
# my_list_copy = [7,5,3,3,2]
# print(my_list)
# user_input = int(input("Ввести число: "))
# my_list.insert(-1,user_input)
# my_list=sorted(my_list)
# print(list(reversed(my_list)))
# >>>>>>> master
