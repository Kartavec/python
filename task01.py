import time


def countdown(seconds):
    for i in range(seconds):
        print(f'{seconds - i} seconds...')
        time.sleep(1)


class TrafficLight:
    __color = None

    def running(self):
        while True:
            self.__color = 'RED'
            print(f'Light is {self.__color}')
            countdown(7)
            self.__color = 'YELLOW'
            print(f'Light is {self.__color}')
            countdown(2)
            self.__color = 'GREEN'
            print(f'Light is {self.__color}')
            countdown(5)


if __name__ == '__main__':
    myTF = TrafficLight()
    myTF.running()
