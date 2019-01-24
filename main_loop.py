from Player import Player
from actions.BoardAction import GrainSeeds

player = Player(uid=1)

print(player.display_player())

for i in range(5):
    player.do(GrainSeeds())

print(player.display_player())
