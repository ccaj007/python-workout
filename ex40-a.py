class Person():
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def __del__(self):
        Person.population -= 1

class Transaction():
    balance = 0

    def __init__(self, amount):
        self.amount = amount
        Transaction.balance += amount


