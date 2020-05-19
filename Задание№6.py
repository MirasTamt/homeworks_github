# <<<<<<< Homework#3
# # 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# # Например, print(int_func(‘text’)) -> Text.
# # Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# # Каждое слово состоит из латинских букв в нижнем регистре.
# # Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# def int_func(text):
#     return str(text).title()
# print(int_func('text'))

# user_input=(input('Type words in latin: ').lower().split(' '))
# for word in user_input:
#     print(int_func(word))

# =======
# goods=[
# (1, {'name': input('insert type of good#1: '), 'price': input('insert price of good#1: '), 'qty': input('insert qty of good#1: '), 'ud': input('insert value of qty: ')}),
# (2, {'name': input('insert type of good#2: '), 'price': input('insert price of good#2: '), 'qty': input('insert qty of good#2: '), 'ud': input('insert value of qty: ')}),
# (3, {'name': input('insert type of good#3: '), 'price': input('insert price of good#3: '), 'qty': input('insert qty of good#3: '), 'ud': input('insert value of qty: ')})
# ]
# dict_1=goods[0][1]
# dict_2=goods[1][1]
# dict_3=goods[2][1]

# keys_in_list_1 = list(dict_1.keys())
# values_in_list_1=list(dict_1.values())
# values_in_list_2=list(dict_2.values())
# values_in_list_3=list(dict_3.values())
# print(keys_in_list_1)
# print(values_in_list_1)

# list_names = [values_in_list_1[0],values_in_list_2[0],values_in_list_3[0]]
# list_price = [values_in_list_1[1],values_in_list_2[1],values_in_list_3[1]]
# list_qty = [values_in_list_1[2],values_in_list_2[2],values_in_list_3[2]]
# set_ud = list(set([values_in_list_1[3],values_in_list_2[3],values_in_list_3[3]]))


# print(list_names)
# goods_analyze = { keys_in_list_1[0]:list_names, keys_in_list_1[1]:list_price, keys_in_list_1[2]:list_qty, keys_in_list_1[3]:set_ud}
# print(goods_analyze)
# >>>>>>> master
