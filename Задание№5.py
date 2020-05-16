my_list = [7, 5, 3, 3, 2]
print(type(my_list))
my_list_copy = [7,5,3,3,2]
print(my_list)
user_input = int(input("Ввести число: "))
my_list.insert(-1,user_input)
my_list=sorted(my_list)
print(list(reversed(my_list)))