"""1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time



class TrafficLight:
    __signal_colors = ['Красный', 'Желтый', 'Зеленый']
    @staticmethod
    def running():
        print(TrafficLight.__signal_colors[0])
        #time.sleep(7)
        print(TrafficLight.__signal_colors[1])
        #time.sleep(2)
        print(TrafficLight.__signal_colors[2])
        #time.sleep(10)

tr_lght = TrafficLight
tr_lght.running()



print('------------------------------------------------------------------------------------------')



"""2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
"""



class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def calcuate(self):
        print('Расчет массы асфальта дороги:')
        print(f'Ширина дороги {self._width} см')
        print(f'Длина дороги {self._lenght} см')
        print(f'При толщине асфальта 12 см масса асфальта составит '
              f'{(self._width * self._lenght * 12 * 25) / 10000000} т')

road_1 = Road(10000, 600)
road_1.calcuate()



print('------------------------------------------------------------------------------------------')



"""3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода 
с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров.
"""



class Worker:
    def __init__(self, worker_name, worker_surname, worker_position, wage, bonus):
        self.worker_name = worker_name
        self.worker_surname = worker_surname
        self.worker_position = worker_position
        self._worker_income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, worker_name, worker_surname, worker_position, wage, bonus):
        super().__init__(worker_name, worker_surname, worker_position, wage, bonus)
    def get_full_name(self):
        print(f'{self.worker_name} {self.worker_surname}')
    def get_total_income(self):
        income = self._worker_income['wage'] + self._worker_income['bonus']
        print(f'Доход сотрудика с учетом премии {income}')

employee = Position('Андрей', 'Петров', 'торговый агент', 30000, 80000)
print(employee.worker_name)
print(employee.worker_surname)
print(f'зарплата сотрудника {employee._worker_income["wage"]}')
print(f'премия сотрудника {employee._worker_income["bonus"]}')
employee.get_full_name()
employee.get_total_income()


print('------------------------------------------------------------------------------------------')



"""4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, 
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) 
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, direction, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self):
        if self.direction == 'right' :
            print(f'Машина {self.name} повернула направо')
        elif self.direction == 'left' :
            print(f'Машина {self.name} повернула налево')
        else:
            print('Неверно указано направлеие поворота')

    def showspeed(self):
        print(f'Машина двигается со скоростью {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, direction, is_police):
        super().__init__(speed, color, name, direction, is_police)

    def showspeed(self):
        if self.speed > 60:
            print('Машина двигается с превышением скорости')
        else:
            print(f'Машина двигается со скоростью {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name, direction, is_police):
        super().__init__(speed, color, name, direction, is_police)

    def showspeed(self):
        if self.speed > 40:
            print('Машина двигается с превышением скорости')
        else:
            print(f'Машина двигается со скоростью {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, direction, is_police):
        super().__init__(speed, color, name, direction, is_police)

    def showspeed(self):
        print(f'Машина двигается со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, direction, is_police):
        super().__init__(speed, color, name, direction, is_police)

    def showspeed(self):
        print(f'Машина двигается со скоростью {self.speed} км/ч')


car_1 = TownCar(90, 'Красный', 'Линкольн', 'left', False)

print(f'Машина номер один {car_1.color} {car_1.name}')
print(car_1.is_police)
car_1.go()
car_1.showspeed()
car_1.turn()
car_1.stop()


car_2 = WorkCar(60, 'Синий', 'ГАЗ-66', 'right', False)

print(f'Машина номер один {car_2.color} {car_2.name}')
print(car_2.is_police)
car_2.go()
car_2.showspeed()
car_2.turn()
car_2.stop()

car_3 = SportCar(260, 'Черный', 'Koenigsegg', 'right', False)

print(f'Машина номер один {car_3.color} {car_3.name}')
print(car_3.is_police)
car_3.go()
car_3.showspeed()
car_3.turn()
car_3.stop()

car_4 = PoliceCar(60, 'Белый', 'Dodge', 'left', True)

print(f'Машина номер один {car_4.color} {car_4.name}')
print(car_4.is_police)
car_4.go()
car_4.showspeed()
car_4.turn()
car_4.stop()



print('------------------------------------------------------------------------------------------')

"""5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение 
«Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен 
выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    @staticmethod
    def draw():
        print('Рисуем ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    @staticmethod
    def draw():
        print('Рисуем карандашом')


class Marker(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'У нас в руках {self.title}. Рисуем {self.title}ом')

draw_1 = Pen('ручка')
draw_2 = Pencil('карандаш')
draw_3 = Marker('маркер')

Stationery.draw()

draw_1.draw()
draw_2.draw()
draw_3.draw()


