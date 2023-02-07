# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
# 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} едет'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} перевернулся в право'

    def turn_left(self):
        return f'{self.name} перевернулся в лево'

    def show_speed(self):
        return f'Скорость {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость городского автомобиля  {self.name} равна {self.speed}')

        if self.speed > 40:
            return f' {self.name} привысил скорость'
        else:
            return f'{self.name} без привышения скорости'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочего автомобиля {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} полицейская машина'


gaz = SportCar(100, 'красный', 'ГАЗ', False)
zaz = TownCar(30, 'белый', 'ЗАЗ', False)
lada = WorkCar(70, 'желтый', 'Лада', True)
uaz = PoliceCar(110, 'синий', 'Ford', True)
print(lada.turn_left())
print(f'Когда {zaz.turn_right()}, тогда {gaz.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name} имеет цвет {lada.color}')
print(f'{gaz.name} полицейский автомобиль? {gaz.is_police}')
print(f'{lada.name}  полицейский автомобиль? {lada.is_police}')
print(gaz.show_speed())
print(zaz.show_speed())
print(uaz.police())
print(uaz.show_speed())
