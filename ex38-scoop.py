
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Beverage():
    def __init__(self, name, temperature=75):
        self.name = name
        self.temperature = temperature

class LogFile():
    def __init__(self, filename):
        self.filename = open(filename, 'w')

def create_scoops():
    scoops = [Scoop(flavor) for flavor in ('chocolate', 'vanilla', 'persimmon')]
    for scoop in scoops:
        print(scoop.flavor)

create_scoops()

