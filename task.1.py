import time,itertools
class TrafficLight:
    def __init__(self):
        self.__color = ["RED", "YELLOW", "GREEN"]
    def running(self):
        for i in itertools.cycle(self.__color):
            if i == 'YELLOW':
                time.sleep(5)
            elif i == 'GREEN':
                time.sleep(2)
            elif i == "RED":
                time.sleep(7)
            print(i)

road = TrafficLight()
road.running()

