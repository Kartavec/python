class Stationery:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


for st in (Pen('Pen'), Pencil('Pencil'), Handle('Handle')):
    st.draw()
