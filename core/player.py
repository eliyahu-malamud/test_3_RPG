import random

class Player:
    flag = random.randint(0, 20)
    def __init__(self, name):
        self.name = name
        self.speed = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15)
        if Player.flag > 10:
            self.profession = 'player'
            self.hp = 50
            self.power = random.randint(5, 10) + 2
        else:
            self.profession = 'doctor'
            self.hp = 60
            self.power = random.randint(5, 10)

    def speak(self):
        return f'hi I am {self.name} and I am going to win. hello!!'
    def attack(self):
        a = random.randint(1, 20)
        return a + self.speed








