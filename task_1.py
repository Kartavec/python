
import time
from itertools import cycle

class TrafficLight:
    __modes = (('red', 7), ('yellow', 2), ('green', 5), ('yellow', 2))
    __light_start = 0
    __next_light = 0

    def __init__(self):
        self.__color = self.__modes[0][0]
        self.__tic()

    def running(self):

        prew_color = None
        while True:
            self.__tic()
            if prew_color != self.__color:
                prew_color = self.__color
                print(self.__color)

    def __tic(self):

        if self.__light_start + dict(self.__modes)[self.__color] <= time.time():
            self.__color, self.__light_start = self.__modes[self.__next_light][0], time.time()
            self.__next_light = self.__next_light + 1 if len(self.__modes) > self.__next_light + 1 else 0

    def color(self):
        self.__tic()
        return self.__color


if __name__ == '__main__':
    lighter = TrafficLight()
    time.sleep(0.5)
    lighter2 = TrafficLight()
    time.sleep(0.5)
    lighter3 = TrafficLight()
    time.sleep(0.5)
    for light in cycle((lighter, lighter2, lighter3)):
        print(light.color())
        time.sleep(1)
