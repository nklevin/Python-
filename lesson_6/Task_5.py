class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Start rendering {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took the {self.title}. Start pen drawing'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took the {self.title}. Start pencil drawing'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took the {self.title}. Start marker drawing'


pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
