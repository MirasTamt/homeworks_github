# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
my_list =[]
with open('translate.txt','r+') as file:
    content = file.readlines()
    for word in content:
        my_list.append(word.split(' — '))
    for number in my_list:
        if number[0] == 'One':
            number.remove('One')
            number.insert(0,'Один -')
            file.writelines(number)
        elif number[0] == 'Two':
            number.remove('Two')
            number.insert(0,'Два -')
            file.writelines(number)
        elif number[0] == 'Three':
            number.remove('Three')
            number.insert(0,'Три -')
            file.writelines(number)
        elif number[0] == 'Four':
            number.remove('Four')
            number.insert(0,'Четыре -')
            file.writelines(number)


        # elif my_list[2][0] == 'Three':
        #     my_list.remove([2][0])
        #     my_list.insert([2][0],'Три')
        # elif my_list[3][0] == 'Four':
        #     my_list.remove([3][0])
        #     my_list.insert([3][0],'Четыре')
# print(number)
        # print(my_list)
        # if my_list[0][0] == 'One':
        #     my_list.pop[0][0]
        #     my_list.insert([0][0],'Один')
        # #     my_list.remove([0][0])
        #     my_list.insert([0][0],'Один')
        # elif my_list[1][0] == 'Two':
        #     my_list.remove([1][0])
        #     my_list.insert([1][0],'Два')
        # elif my_list[2][0] == 'Three':
        #     my_list.remove([2][0])
        #     my_list.insert([2][0],'Три')
        # elif my_list[3][0] == 'Four':
        #     my_list.remove([3][0])
        #     my_list.insert([3][0],'Четыре')
# print(my_list)