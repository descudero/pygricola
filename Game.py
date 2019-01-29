from Player import Player
from Board import Board
from pydispatch import dispatcher

class Game:
    def __init__(self, number_players=1):
        self.players = [Player(uid=uid) for uid in range(stop=number_players)]
        self.board = Board(number_players=number_players)
