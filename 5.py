class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start Drawing')


class Pen(Stationery):
    def draw(self):
        print('Start Pen Drawing')


class Pencil(Stationery):
    def draw(self):
        print('Start Pencil Drawing')


class Handle(Stationery):
    def draw(self):
        print('Start Handle Drawing')


pen1 = Pen('My pen')
pen1.draw()

pencil1 = Pencil("Nadya's pencil")
pencil1.draw()

handle1 = Handle("Bob'b handle")
handle1.draw()

