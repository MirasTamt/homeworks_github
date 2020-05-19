# <<<<<<< homework#2
# number_in_list = int(input("Введите количество желаемых элементов в списке: "))
# my_list = []
# while len(my_list)<number_in_list:
#     my_list.append(input("Введите любой элемент в список: "))
# print(my_list)
# if len(my_list)%2 == 0:
#     for i in range(0,len(my_list),2):
#             my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
# else:
#     my_list_popped = my_list.pop(-1)
#     for i in range(0,len(my_list),2):
#         my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
#     my_list.append(my_list_popped)


# print(my_list)
# =======
# # 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

# seconds=int(input("Введите время в секундах: "))
# minutes = seconds/60
# hours = minutes/60
# left_seconds = int((minutes - int(minutes))*60)
# left_minutes = int((hours-int(hours))*60)

# def converter(below_10_digit):
#     below_10_digit=round(below_10_digit,None)
#     return "0" + str(below_10_digit)

# if seconds < 60:
#     if seconds < 10:
#        seconds=converter(seconds)
#     print(f"Вы ввели время 00:00:{(seconds)}")
# elif seconds > 60 and seconds < 3600:
#     if left_seconds < 10:
#         left_seconds = converter(left_seconds)
#         pass
#     if minutes < 10:
#         minutes=converter(minutes)
#         pass
#     else: minutes = int(minutes)
#     print((f"Вы ввели время 00:{(minutes)}:{left_seconds}"))
# elif seconds > 3600 and seconds < 86400:
#     if left_seconds < 10:
#         left_seconds = converter(left_seconds)
#         pass
#     if minutes < 10:
#         minutes=converter(minutes)
#         pass
#     else: minutes = int(minutes)
#     if left_minutes < 10:
#         left_minutes = converter(left_minutes)
#         pass
#     if hours < 10:
#         hours = converter(hours)
# #         pass
# #     else: hours = int(hours)
# #     print((f"Вы ввели время {hours}:{(left_minutes)}:{left_seconds}"))


# >>>>>>> master
