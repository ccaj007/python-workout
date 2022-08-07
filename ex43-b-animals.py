class Animal():
    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.sound} - {self.color} {self.species}, {self.number_of_legs} legs'

class ZeroLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 0

class TwoLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 2

class FourLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 4

class Sheep(FourLeggedAnimal):
    sound = 'Baa'
    
    def __init__(self, color):
        super().__init__(color)


class Wolf(FourLeggedAnimal):
    sound = 'Howl'

    def __init__(self, color):
        super().__init__(color)


class Snake(ZeroLeggedAnimal):
    sound = 'Hss'

    def __init__(self, color):
        super().__init__(color)


class Parrot(Animal):
    number_of_legs = 2
    sound = 'Polly'

    def __init__(self, color):
        super().__init__(color)


wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')
print(wolf)
print(sheep)
print(snake)
print(parrot)