class Stationery:
    title: str

    @staticmethod
    def draw():
        print("Запуск отрисовки.")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print(f'{self.title} пишет.')


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print(f'{self.title} штрихует.')


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print(f'{self.title} обводит.')


if __name__ == '__main__':
    stationery = Stationery()
    stationery.draw()

    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()
