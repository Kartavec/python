class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print("""   
        | | |   
        | | |   
        | | |   
        |_|_|   
        \\   /    
         \\-/  
        """)


class Pen(Stationery):
    def draw(self):
        print("""   
        |   |   
        |   |   
        |===|   
        |___|   
         ).(     
         \\|/ 
         """)


class Handle(Stationery):
    def draw(self):
        print("""   
        |   |   
        |   |   
        )---(   
        |___|   
         [_]    
          U 
         """)


if __name__ == '__main__':
    my_st = Stationery('qwe')
    my_st.draw()

    my_pen = Pen('Pilot')
    my_pen.draw()

    my_pencil = Pencil('Faber Castle')
    my_pencil.draw()

    my_handle = Handle('Permanent handle')
    my_handle.draw()
