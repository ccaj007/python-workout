# for index, letter in enumerate('abc'):
#     print(f'{index}: {letter}')

class MyEnumerate():
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __repr__(self):
        for i in self.s:
            print(i)

a = MyEnumerate('abc')
print(a)