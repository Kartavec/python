"""
Задание 4.
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы:
go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод
show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышениискорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""


class Car:
    _registry = []

    def __init__(self, speed=None, color=None, name=None, is_police=False):
        self._registry.append(self)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return self.name + ' - машина поехала'

    def stop(self):
        return self.name + ' - машина остановилась'

    def turn(self, direction):
        return self.name + ' повернула ' + direction

    def get_show_speed(self, max_speed=None):
        speed_message = f'{self.name}\nТекущая скорость: {self.speed}'
        return speed_message


class TownCar(Car):

    def get_show_speed(self, max_speed=40):
        message_error = ''
        if max_speed:
            if self.speed > max_speed:
                message_error = f'''
                    Превышение скорости на {self.speed - max_speed}!
                    Максимальная скорость: {max_speed}
                    '''

        return super().get_show_speed() + message_error


class SportCar(Car):
    pass


class WorkCar(Car):

    def get_show_speed(self, max_speed=60):
        message_error = ''
        if max_speed:
            if self.speed > max_speed:
                message_error = f'''
                    Превышение скорости на {self.speed - max_speed}!
                    Максимальная скорость: {max_speed}
                    '''
        super().get_show_speed()
        return super().get_show_speed() + message_error


class PoliceCar(Car):
    pass


town_car = TownCar(140, 'Серая', 'Городская машина')
sport_car = SportCar(240, 'Красная', 'Спортивная машина')
work_car = WorkCar(60, 'Желтая', 'Рабочая машина')
police_car = PoliceCar(210, 'Синяя', 'Полицейская машина', True)

for car in Car._registry:
    print('Название: {}, цвет: {}, текущая скорость: {}, полицейская: {}'
          .format(car.name, car.color, car.speed, car.is_police))
print(work_car.get_show_speed())
print(sport_car.stop())
print(town_car.go())
print(police_car.turn('налево'))
