from Player import Player
from actions.BoardAction import *
from pydispatch import dispatcher
from Board import Board


player = Player(uid=1)
board = Board(number_players=2)



print(player.display_player())
cp = ClayPit(board)

for i in range(3):
    board.upkeep()
    board.end()
for i in range(1):
    player.do(cp)
for i in range(1):
    board.upkeep()
    board.end()
for i in range(1):
    player.do(cp)
print(player.display_player())
