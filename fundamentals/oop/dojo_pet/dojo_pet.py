class Pet():
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25 
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print('Meowwwwwwww!')
        return self

pet1 = Pet('Bao', 'Pomsky', 'Roll over')
pet2 = Pet('Fan', 'Corgi', 'Fetch')

class Ninja():
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.lasy_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self

ninja1 = Ninja('Dan', 'Mullenay', pet1, 'Blue Diamond', 'Puppy Food')
ninja2 = Ninja('Julien', 'Auza', pet2, 'Blue Buffalo', 'Adult Food')

ninja1.walk().feed().bathe()
print(pet1.health)

ninja2.walk().feed().walk().feed().bathe().play().feed().bathe()
print(pet2.health, pet2.energy)