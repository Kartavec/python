# Class 06
# Task 01
# A  script that creates Traficc lights class

from time import sleep


class TrafficLights:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i < 3:
            print(f'The traffic lights are switching \n '
                  f'{TrafficLights.__color[i]}')
            if i == 0:
                sleep(2)
            elif i == 1:
                sleep(3)
            elif i == 2:
                sleep(1)
            i += 1


trafficlight = TrafficLights()
trafficlight.running()
