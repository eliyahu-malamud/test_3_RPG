import random

class Goblin:
    flag = random.randint(0, 30)
    def __init__(self, name):
        self. name = name
        self.hp = 20
        self.type = 'goblin'
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
        if Goblin.flag > 10:
            w = 'knife'
        elif Goblin.flag > 20:
            w = 'sord'
        else:
            w = 'hax'
        self.weapon = w
    def speak(self):
        return f'hi I am angry {self.name}. give up now!!'
    def attack(self):
        a = random.randint(1, 20)
        return a + self.speed
    def run_away(self):
        pass