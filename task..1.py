
new_matrix =[]
class Matrix:
    def __init__(self,list_of_matrix):
        self.list_of_matrix = list_of_matrix

    def __str__(self):
        return (f'Matrix is: {self.list_of_matrix}')
    def __add__(self, other):
        for i in range(len(self.list_of_matrix)):
            new_matrix.append(list(self.list_of_matrix)[i] + list(other.list_of_matrix)[i])

my_matrix = Matrix([2,3,4,5,66,8])
my_matrix2 = Matrix([3,4,6,67,8,9])
print(my_matrix)
print(my_matrix2)
my_matrix+my_matrix2
print(my_matrix)