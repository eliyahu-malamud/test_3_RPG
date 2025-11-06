from core import goblin, orc
from core import player as p
import game
def play_game():
    player = game.Game.create_player()
    monster = game.Game.choose_random_monster()
    game.Game.battle(player, monster)

play_game()
