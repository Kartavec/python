class Car:
    def __init__(self, speed, color, name, is_police=False):
        if not isinstance(is_police, bool):
            raise TypeError('is_police attribute must be boolean')
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} goes!')

    def stop(self):
        print(f'Car {self.name} stops!')

    def turn(self, direction):
        print(f'Car {self.name} turn {direction}')

    def show_speed(self):
        print(f'Car {self.name} speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Over Speed!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Over Speed!')


class PoliceCar(Car):
    def __init__(self, *args):
        police_args = list(args[:3])
        police_args.append(True)
        super().__init__(*police_args)


car1 = Car(100, 'green', 'Fiat')
print(car1.is_police)

car1.go()
car1.turn('Left')
car1.stop()
car1.show_speed()

work_car = WorkCar(120, 'yellow', 'City Cat')
work_car.show_speed()

pc = PoliceCar(40, 'blue', 'BMW')
print(pc.is_police)
