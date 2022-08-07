class NotEnoughPostageError(Exception):
    pass

class Envelope():
    postage_weight = 10

    def __init__(self, weight):
        self.weight = weight
        self.postage = 0
        self.was_send = False

    def add_postage(self, amount):
        self.postage += amount

    def send(self):
        if self.postage >= self.weight * self.postage_weight:
            print(f'sending: {self.postage}')
            self.was_send = True
        else:
            raise NotEnoughPostageError('Not enough postage')


class BigEnevelope(Envelope):
    postage_weight = 15

a = Envelope(2)
#a.send()
print(a.was_send)
b = Envelope(6)
b.add_postage(100)
print(b.postage)
b.send()

print(b.was_send)