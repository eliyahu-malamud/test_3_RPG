import random

class Orc:
    flag = random.randint(0, 30)
    def __init__(self, name):
        self. name = name
        self.hp = 50
        self.type = 'orc'
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)
        if Orc.flag > 10:
            w = 'knife'
        elif Orc.flag > 20:
            w = 'sord'
        else:
            w = 'hax'
        self.weapon = w
    def speak(self):
        return f'hi I am angry {self.name}. give up now!!'
    def attack(self):
        a = random.randint(1, 20)
        return a + self.speed
