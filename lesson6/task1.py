# Остановка выполнения кода не предусмотрена (только принудительное завершение 
# пользователем).
# Встроен таймер обратного отсчета до переключения сигнала светофора.
# Ошибка в порядке смены режимов сигналов светофора исключена!

import time

class TrafficLight():

    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            if self.__color == 'red':
                l_time = 7
                print('The traffic light is RED now.')
                while l_time > 0:
                    print(l_time)
                    time.sleep(1)
                    l_time -= 1
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                l_time = 2
                print('The traffic light is YELLOW now.')
                while l_time > 0:
                    print(l_time)
                    time.sleep(1)
                    l_time -= 1
                self.__color = 'green'
            elif self.__color == 'green':
                l_time = 5
                print('The traffic light is GREEN now.')
                while l_time > 0:
                    print(l_time)
                    time.sleep(1)
                    l_time -= 1
                self.__color = 'red'
                
my_light = TrafficLight('green')
my_light.running()

