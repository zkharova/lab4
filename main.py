class Entity:
    name = ""
    status = "Alive"
    health = 0
    heal = 0
    base_damage = 0
    equipped = None

    def healing(self,):
        self.health += self.heal


    def attack(self, enemy):
        if enemy.status == "Alive":
            if self.equipped is not None:
                damage = self.equipped.damage
            else:
                damage = self.base_damage
            enemy.health -= damage
            enemy.check()

    def check(self):
        if self.health <= 0:
            self.health = 0
            self.status = "Dead"

    def equip(self, Item):
        self.equipped = Item

    def __repr__(self):
        return "Entity: {}, Status: {}, Health: {}, Equipped: {}".format(
            self.name, self.status, self.health, self.equipped
        )



class Teammate(Entity):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "Player: {}, Health: {}, Equipped: {}".format(
            self.name, self.health, self.equipped
        )





class Carry(Teammate):
    def __init__(self):
        super().__init__()
        self.name = "Sven"
        self.health = 1600
        self.heal = 50
        self.base_damage = 140

class Support(Teammate):
    def __init__(self):
        super().__init__()
        self.name = "Pudge"
        self.health = 1350
        self.heal = 60
        self.base_damage = 110

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Roshan"
        self.health = 10000
        self.heal = 500
        self.base_damage = 130

class Item:
    name = ""
    damage = 0
    heal = 0



class Weapon(Item):

    def __init__(self):
        super().__init__()
        self.type = "weapon"

    def __repr__(self):
        return "{0}, dmg: {1}".format(" ".join([self.name]), self.damage)


class Desolator(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Desolator"
        self.damage = 120

class HearthOfTarascque(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Tarasq"
        self.damage = 10
        self.heal = 100


pos1 = Carry()
print(pos1)

pos5 = Support()
print(pos5)

desol = Desolator()
tarasq = HearthOfTarascque()

pos1.equip(desol)
print(pos1)

pos5.equip(tarasq)
print(pos5)

roshan = Enemy()

roshan.attack(pos5)
print(pos5)
roshan.attack(pos5)
print(pos5)
roshan.attack(pos5)
print(pos5)

pos5.healing()
print(pos5)

pos1.attack(roshan)
print(roshan)
