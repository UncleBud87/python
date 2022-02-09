
class Pet():

    def __init__(self, name, type, tricks, energy, health):
        self.pet = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health

    def sleep(self):
        self.energy = + 25
        print(f"{self.name} sleeps, ENERGY: {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health += +10
        print(f"{self.name} eats, ENERGY: {self.energy}")
        return self

    def play(self):
        self.health += 5
        self.energy -= 5
        print(f"{self.name} plays, HEALTH: {self.health} ENERGY: {self.energy}")
        return self

    def noise(self):
        print("woof")


