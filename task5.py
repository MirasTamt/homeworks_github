# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
#
i=0
my_list = []
my_list2 =[]
with open('task5.txt','w') as file:
    file.write(input('Insert number:'))
with open('task5.txt') as file:
    content = file.readlines()
    for number in content:
        my_list.append(number.split())
    for i in my_list[0]:
        my_list2.append(int(i))
    print(sum(my_list2))

