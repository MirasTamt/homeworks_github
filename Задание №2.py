number_in_list = int(input("Введите количество желаемых элементов в списке: "))
my_list = []
while len(my_list)<number_in_list:
    my_list.append(input("Введите любой элемент в список: "))
print(my_list)
for i in my_list:
    popped=my_list.pop(my_list.index(i))
    my_list.insert(1,popped)
    print(my_list)

    # my_list[my_list.index(i)],my_list[my_list.index(i+1)]=my_list[my_list.index(i)+1],my_list[my_list.index(i)]
    # print(my_list)
    # print(my_list[(my_list.index(i)+1)])
