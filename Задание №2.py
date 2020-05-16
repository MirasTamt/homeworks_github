number_in_list = int(input("Введите количество желаемых элементов в списке: "))
my_list = []
while len(my_list)<number_in_list:
    my_list.append(input("Введите любой элемент в список: "))
print(my_list)
if len(my_list)%2 == 0:
    for i in range(0,len(my_list),2):
            my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
else:
    my_list_popped = my_list.pop(-1)
    for i in range(0,len(my_list),2):
        my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
    my_list.append(my_list_popped)


print(my_list)