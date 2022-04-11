class Car:
    def __init__(self,
                 speed: float, color: str,
                 name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        print(f'The speed of {self.name} is {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()

        if self.speed > 60:
            print(f'The speed of {self.name} is higher than allowed')
        else:
            print(f'The speed of {self.name} is normal')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()

        if self.speed > 40:
            return f'The speed of {self.name} is higher than allowed'
        else:
            return f'The speed of {self.name} is normal'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police_car(self):
        if self.is_police is True:
            return f'{self.name} is a police car'
        else:
            return f'{self.name} is not a police car'


ferrari = SportCar(200, 'red', 'fiorano', False)
chevrolet = PoliceCar(100, 'red', 'silverado', True)
audi = TownCar(60, 'red', 'audi a4', False)
ferrari.show_speed()
chevrolet.show_speed()
audi.show_speed()
