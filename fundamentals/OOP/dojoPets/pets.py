
class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100

    def sleep(self):
        self.energy += 25
        print(f"{self.name} sleeps, ENERGY: {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} eats, ENERGY: {self.energy}")
        return self

    def play(self):
        self.health += 5
        self.energy -= 5
        print(f"{self.name} plays, HEALTH: {self.health} ENERGY: {self.energy}")
        return self

    def noise(self):
        print("woof")

    def display(self):
        print(
            f'name: {self.name}, type: {self.type}, tricks: {self.energy}, health: {self.health}')
        return self


class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        self.pet.display()
        return self

    def feed(self):
        self.pet.eat()
        self.pet.display()
        return self

    def bathe(self):
        self.pet.noise()
        self.pet.display()
        return self



maverick = Pet("Maverick", "Aussy", "Jump")
john = Ninja("John", "Smith", "bacon", "merrick", maverick)

john.walk().feed().bathe()

# maverick.sleep().display().eat().display().play().display().noise()
