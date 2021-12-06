# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    _title = ""

    def __init__(self):
        self._title = "Канцелярская принадлежность"

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):

    def __init__(self):
        self._title = "Ручка"

    def draw(self):
        print(f'{self._title}. Начала писать слово "Кракен"')


class Pencil(Stationery):

    def __init__(self):
        self._title = "Карандаш"

    def draw(self):
        print(f'{self._title}. Начал рисовать чертеж')


class Hendle(Stationery):

    def __init__(self):
        self._title = "Маркер"

    def draw(self):
        print(f'{self._title}. Начал выделять текст')

p1 = Pen()
p1.draw()
p2 = Pencil()
p2.draw()
m1 = Hendle()
m1.draw()