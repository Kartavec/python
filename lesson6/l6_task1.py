from time import sleep


class TrafficLight:
    __color = {'Red': 7, 'Yellow': 2, 'Green': 10}

    def running(self):
        while True:
            for key, value in self.__color.items():
                print(key)
                sleep(value)


traffic = TrafficLight()
traffic.running()

