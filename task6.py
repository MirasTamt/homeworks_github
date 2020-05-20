from itertools import count,cycle

"""Iterator#1"""

c=0
for number in count(3):
    if c > 7:
        break
    else:
        print(number)
        c += 1


"""Iterator#2"""
i=0
my_list = [1,2,4,5,6,789,0]
for loop in cycle(my_list):
    if i>15:
        break
    else:
        print(loop)
        i+=1