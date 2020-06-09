class Car:
    _speed = 0
    _is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self, speed):
        self._speed = speed
        print(f'Автомобиль двигается со скоростью {speed} км/ч')

    def stop(self):
        self._speed = 0
        print('Автомобиль остановился')

    def turn(self, direction):
        if self._speed > 0:
            print(f'Автомобиль повернул {direction}')
        else:
            print('Нельзя поворачивать на стоящем автомобиле')

    def show_speed(self):
        print(f'Скорость автомобиля - {self._speed} км/ч')

    def siren(self):
        if self._is_police is True:
            print('Gaga')
        else:
            print('Gaga in available only on police car!')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля - {self._speed} км/ч')
        if self._speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!!!')


class SportCar(Car):
    def drift(self):
        if self._speed > 0:
            print(f'{self.name} is drifting on {self.color} car')
        else:
            print("You cann't drift with no speed")


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля - {self._speed} км/ч')
        if self._speed > 60:
            print('ПРЕВЫШЕНИЕ СКОРОСТИ!!!')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self._is_police = True


if __name__ == '__main__':
    my_pc = PoliceCar('black', 'Steeve')
    my_pc.siren()

    my_tc = TownCar('yellow', 'Barbara')
    my_tc.go(120)
    my_tc.show_speed()

    my_sc = SportCar('white', 'Robert')
    my_sc.drift()
    my_sc.go(300)
    my_sc.drift()
    my_sc.turn('влево')
    my_sc.turn('вправо')
    my_sc.stop()
    my_sc.show_speed()
    my_sc.turn('вправо')
    my_sc.siren()