class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police == True:
            print('\nIt is police car.')

    def go(self):
        print('The car is going straight.')
    def stop(self):
        print('The car stopped.')
    def turn_left(self):
        print('The car turned left.')
    def turn_right(self):
        print('The car turned right.')
    def show_speed(self):
        print(f'The speed is {self.speed} km/h.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('\nIt is town car.')
    def show_speed(self):
        if self.speed > 60:
            print(f'The car is going too fast - {self.speed} km/h.')
        else:
            print(f'The speed is {self.speed} km/h.')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('\nIt is sport car.')
    

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print('\nIt is work car.')
    def show_speed(self):
        if self.speed > 40:
            print(f'The car is going too fast - {self.speed} km/h.')
        else:
            print(f'The speed is {self.speed} km/h.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


police_car = PoliceCar(100, 'red_blue', 'Dodge', True)
police_car.go()
police_car.turn_left()
police_car.show_speed()

work_car = WorkCar(43, 'yellow', 'skoda', False)
work_car.go()
work_car.stop()
work_car.show_speed()

sport_car = SportCar(150, 'black', 'audi', False)
sport_car.go()
sport_car.turn_right()
sport_car.turn_left()
sport_car.go()
sport_car.show_speed()

town_car = TownCar(55, 'grey', 'honda', False)
town_car.go()
town_car.turn_left()
town_car.stop()
town_car.go()
town_car.show_speed()


