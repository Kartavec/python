import random


class Car:
    _speed = 0
    _is_police = False

    def __init__(self, name, color):
        self.color = color
        self.name = name

    def __str__(self):
        return 'Car: %s (%s)' % (self.name, self.color)

    def go(self, speed):
        self._speed = speed
        self.show_speed()

    def stop(self):
        self._speed = 0
        self.show_speed()

    def turn(self, direction):
        if self._speed > 0:
            print('%s turn %s' % (self, direction))
        else:
            print('%s stopped and can`t turn' % self)

    def show_speed(self):
        if self._speed == 0:
            print('%s. Stopped' % self)
        else:
            print('%s. Speed %d' % (self, self._speed))
        # return self._speed

    def print_is_police(self):
        if self._is_police:
            print('%s is police' % self)
        else:
            print('%s is not police' % self)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print('over speed')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print('over speed')


class PoliceCar(Car):
    _is_police = True


cars = [
    TownCar('Lada', 'grey'),
    WorkCar('Belaz', 'orange'),
    SportCar('Honda', 'black'),
    PoliceCar('Opel', 'white')
]
turn_list = ['left', 'right', 'around']
for car in cars:
    print(car)
    car.print_is_police()
    car.go(random.randint(0, 60))
    car.go(random.randint(60, 240))
    car.turn(random.choice(turn_list))
    car.stop()
    car.turn(random.choice(turn_list))
    print('')
