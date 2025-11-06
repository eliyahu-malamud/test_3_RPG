import random
from core import orc, goblin
from core import player as p
class Game:
    @staticmethod
    def start():
        while True:
            a = Game.show_game()
            if a == 'p':
                return True
            elif a == 'e':
                return False
            else:
                print('invalid input!!')

    @staticmethod
    def show_game():
        return input("please enter 'p' to play or 'e' to exit:")

    @staticmethod
    def create_player():
        return p.Player('Eliyahu')

    @staticmethod
    def choose_random_monster():
        flag = random.randint(0, 20)
        if flag > 10:
            return orc.Orc('boby')
        else:
            return goblin.Goblin('cody')

    @staticmethod
    def deside_who_first():
        p = Game.roll_dice(6)
        m = Game.roll_dice(6)
        if p > m:
            return 'p'
        elif p < m:
            return 'm'
        else:
            return 'p'

    @staticmethod
    def was_hit(strike_value, enemy_armor):
        if strike_value > enemy_armor:
            return True
        else:
            return False

    @staticmethod
    def battle(player, monster):
            users_choice = Game.start()
            if users_choice:
                if Game.deside_who_first() == 'p':
                    flag = 0
                else:
                    flag = 1
                while True:
                    if flag % 2 == 0:
                        strike = player.attack()
                        result = Game.was_hit(strike, monster.armor_rating)
                        flag += 1
                        if result:
                            damage = player.power + Game.roll_dice(6)
                            monster.hp -= damage
                    elif flag % 2 != 0:
                        strike = monster.attack()
                        result = Game.was_hit(strike, monster.armor_rating)
                        flag += 1
                        if result:
                            if monster.weapon == 'knife':
                                damage = Game.roll_dice(6) * 0.5
                            elif monster.weapon == 'sord':
                                damage = Game.roll_dice(6) * 1
                            else:
                                damage = Game.roll_dice(6) * 1.5
                            player.hp -= damage
                    if player.hp <= 0:
                        print('the monster wind the game!!')
                        break
                    elif monster.hp <= 0:
                        print('the player wind the game!!')
                        break

    @staticmethod
    def roll_dice(sides):
        if sides == 20:
            return random.randint(1, 20)
        else:
            return random.randint(1, 6)


