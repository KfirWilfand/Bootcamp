import random


class Pokemon():
    def __init__(self):
        self.name = 'pokemon'
        self.strength = 0
        self.armor = 0
        self.health = 0
        self.attackNoise = "none"

    def getRandBouns(self):
        return random.randint(1, 4)

    def getAttackNoise(self):
        return self.attackNoise

    def getName(self):
        return self.name

    def isDead(self):
        return self.health <= 0

    def attack(self, defender):
        attakerPwr = self.strength + self.getRandBouns()
        defenderPwr = defender.armor + defender.getRandBouns()

        if attakerPwr > defenderPwr:
            defender.health -= (attakerPwr - defenderPwr)
            return 1
        else:
            return 0


class Pikatchu(Pokemon):
    def __init__(self):
        super()
        self.name = 'pikatchu'
        self.strength = 20
        self.armor = 10
        self.health = 10
        self.attackNoise = "pikkkkathhhh!"


class Aipom(Pokemon):
    def __init__(self):
        super()
        self.name = 'aipom'
        self.strength = 40
        self.armor = 12
        self.health = 10
        self.attackNoise = "aipommmm!"


class Ditto(Pokemon):
    def __init__(self):
        super()
        self.name = 'ditto'
        self.strength = 15
        self.armor = 15
        self.health = 10
        self.attackNoise = "dddddittttttto!"

class Mewtwo(Pokemon):
    def __init__(self):
        super()
        self.name = 'mewtwo'
        self.strength = 40
        self.armor = 42
        self.health = 10
        self.attackNoise = "mewwwtwwwo!"

class Bulbasaur(Pokemon):
    def __init__(self):
        super()
        self.name = 'bulbasaur'
        self.strength = 40
        self.armor = 12
        self.health = 10
        self.attackNoise = "bbbbulbasaaaaaur!"