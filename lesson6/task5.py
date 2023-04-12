class Stationery():
    def __init__(self, title):
       self.title = title
    def draw():
        print('Запуск отрисовки...')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        print("The pen is a perfect choice! Do you want to draw picture? \
Let's get started!")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        print('The pencil is a perfect choice! How about making some notes?')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        print("The handle is a perfect choice! Let's draw!")

pen = Pen(Stationery)
pencil = Pencil(Stationery)
handle = Handle(Stationery)
        

