# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed =speed
        self.color =color
        self.name =name
        self.is_police = is_police
        if self.is_police == True :
            print('It is police Car')
        else:
            print('It is not police Car')

        print(self.name,self.color,self.speed)
    def go(self):
        print('Car drives')
    def stop(self):
        print('Car stops')
    def turn(self,direction):
        print('Car turns {}'.format(direction))


class TownCar(Car):
    def __init__(self,speed,color,name,is_police,show_speed):
        super().__init__(speed,color,name,is_police)
        self.show_speed = show_speed
        if show_speed > 60:
            print('Exceed max. speed, slow down')
    pass

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, show_speed):
        super().__init__(speed, color, name, is_police)
        self.show_speed = show_speed
        if show_speed > 40:
            print('Exceed max. speed, slow down')


class WorkCar(Car):
    pass

class PoliceCar(Car):
    pass


my_corvette = Car(200,'red','Corvette',False)
my_corvette.go()
my_corvette.stop()
my_corvette.turn('right')
my_mini =TownCar('70km/h',"black",'BMW',False,80)
my_police_car = PoliceCar(150, 'black', 'mazda', True)
