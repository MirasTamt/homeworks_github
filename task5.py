from functools import reduce
my_list =[el for el in range(100,1001,1) if el%2==0]
sum_even = reduce(lambda x,y : x+y, my_list)
