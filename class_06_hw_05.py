# Class 06
# Task 05
# A  script that creates class Stationary
# with title as an attribute and draw method.
# The script also creates subclasses Pen, Pencil, Handle 

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'The start of drawing {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. The start of drawing by pen'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. The start of drawing by pencil'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. The start of drawing by highlighter'


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Highlighter')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
