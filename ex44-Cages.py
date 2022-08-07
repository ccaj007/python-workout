class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'

class Sheep(Animal):

    def __init__(self, color):
        super().__init__(color, 4)


class Wolf(Animal):

    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):

    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Cage():
    def __init__(self, id):
        self.id = id
        self.content = []

    def add_animals(self, *animals):
        for animal in animals:
            self.content.append(animal)


    def __repr__(self):
        output = f'Cage {self.id}\n'
        output += '\n'.join('\t' + str(animal) for animal in self.content)
        return output

wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')
c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(snake, parrot)
print(c1)
print(c2)
