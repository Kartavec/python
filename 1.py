from time import sleep


class TrafficLight:
    def __init__(self):
        self._color = 'red'

    def running(self):
        while True:
            if self._color == 'red':
                print('red light')
                sleep(7)
                self._color = 'yellow'
            elif self._color == 'yellow':
                print('yellow light')
                sleep(2)
                self._color = 'green'
            else:
                print('green light')
                sleep(6)
                self._color = 'red'


light1 = TrafficLight()

light1.running()
