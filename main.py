import random


class Animal:
    type = ''
    name = ''
    status = ''
    age = 0
    health = 0
    speed = 0

    def __init__(self, type, name, status, age, health, speed):
        self.type = type
        self.name = name
        self.status = status
        self.age = age
        self.health = health
        self.speed = speed
        print("new ", name, " is created, health = ", health)


def check_status(self):
    if self.health <= 0:
        self.status = 'dead'
        return 'Sorry to say that, but the animal is not alive anymore'
    elif self.health > 0:
        self.status = 'alive'
        return 'Animal is alive now (health = ' + str(self.health) + '). Keep him safe.'


class Carnivore(Animal):
    damage = 0

    def __init__(self, type, name, status, age, health, speed, damage):
        super().__init__(type, name, status, age, health, speed)
        self.damage = damage

    def attack(self, Herbivore):
        if (Herbivore.health <= 0):
            return('Just stop, the animal is already dead')
        else:
            if Herbivore.secrecy > 100:
                tempDamage = random.randint(0, self.damage)
            elif Herbivore.cunning > 100:
                tempDamage = self.damage / 2
            Herbivore.health = Herbivore.health - tempDamage
            if Herbivore.health < 0:
                Herbivore.health = 0
            return ('Ouch! ' + Herbivore.name + ' is hurt. Health points: ' + str(Herbivore.health))





class Wolf(Carnivore):

    def __init__(self):
        super().__init__('Carnivore', 'Wolf', 'alive', 4, 1000, 30, 300)


class Fox(Carnivore):
    def __init__(self):
        super().__init__('Carnivore', 'Fox', 'alive', 3, 1200, 60, 250)


class Herbivore(Animal):
    secrecy = 0
    cunning = 0

    def __init__(self, type, name, status, age, health, speed, secrecy, cunning):
        super().__init__(type, name, status, age, health, speed)
        self.secrecy = secrecy
        self.cunning = cunning

    def attack(self, Animal):
        return ("This animal is herbivore. It doesn't want to attack.")


class Rabbit(Herbivore):

    def __init__(self):
        super().__init__('Herbivore', 'Rabbit', 'alive', 2, 800, 70, 110, 5)


class Duck(Herbivore):

    def __init__(self):
        super().__init__('Herbivore', 'Duck', 'alive', 4, 600, 80, 6, 150)


R = Rabbit()
W = Wolf()

print(check_status(R))
print(check_status(W))

print(R.attack(W))
while R.health > 0:
    print(W.attack(R))

print(W.attack(R))