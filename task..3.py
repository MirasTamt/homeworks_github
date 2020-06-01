ordered_cell =[]
new_cell =[]
class Cell:
    def __init__(self,particles):
        self.particles = list(particles)
        self.number_particles = len(list(particles))
    def __add__(self, other):
        for i in range(self.number_particles):
            self.particles.append(other.particles[i])
        return self.particles
    def __sub__(self, other):
        if self.number_particles > other.number_particles:
            difference = self.number_particles-other.number_particles
            self.particles.clear()
            for i in range(difference):
                self.particles.append(other.particles[-1])
        else:
            return (f'Absence of Master Cell')

    def __mul__(self, other):
        for i in range(self.number_particles*other.number_particles):
            new_cell.append(1)
        return new_cell
    def __truediv__(self, other):
        for i in range(self.number_particles//other.number_particles):
            new_cell.append(1)
        return new_cell

    def make_order(self,order):
        qty_of_set = self.number_particles//order
        for i in range(1,self.number_particles):
            ordered_cell.append('*')
            if i % order == 0:
                ordered_cell.append('\n')
        print(*ordered_cell)





"""test of execution"""
my_cell = Cell([1,1,1,1,1,1,1,1,1,1,1,1])
my_cell.make_order(5)
my_cell2 = Cell([1,1,1,1,1,1])
my_cell/my_cell2
my_cell+my_cell
my_cell-my_cell2
my_cell*my_cell2
print(my_cell.particles)
print(new_cell)


