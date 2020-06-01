from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calc(self):
        pass

class Jacket(Clothes):
        def __init__(self,size):
            super().__init__()
            self.size = size

            @property
            def calc(self):
                return (f'For the Jacket you will need: {float(self.size)/6.5 + 0.5} meters of line')


class Coat(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def calc(self):
        return (f'For the Coat you will need: {float(self.height) *2  + 0.3} meters of line')

my_jacket = Jacket(13)
my_coat = Coat(1.8)
print(my_jacket.calc)
print(my_coat.calc)
