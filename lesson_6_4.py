# . Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, name, color, police=False):
        self.name = name
        self.color = color
        self.is_police = police

    def go(self, speed):
        self.speed = speed
        print(f'Машина {self.name} поехала с скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Машина {self.name} стоит на месте') if self.speed == 0 \
            else print(f'Машина {self.name} едет с скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            Car.show_speed(self)
        else:
            print(f'Машина {self.name} едет с скоростью {self.speed}, превышая скорость')


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            Car.show_speed(self)
        else:
            print(f'Машина {self.name} едет с скоростью {self.speed}, превышая скорость')


tc = TownCar('ВАЗ', "Белый")
tc.show_speed()
tc.go(70)
tc.show_speed()
tc.turn('налево')

