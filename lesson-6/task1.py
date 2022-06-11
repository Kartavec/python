import time
from itertools import cycle

TRAFFIC_LIGHT_COLORS = (
    ('RED', 7),
    ('YELLOW', 2),
    ('GREEN', 5),
)


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        for light in cycle(TRAFFIC_LIGHT_COLORS):
            self.__color = light[0]
            print(f'Color: {self.__color}. Sleep: {light[1]}s')
            time.sleep(light[1])


tl = TrafficLight()
tl.running()
