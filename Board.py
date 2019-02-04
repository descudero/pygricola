from pydispatch import dispatcher

class Board:
    def __init__(self, game, number_players=1):
        self.game = game
        self.board_actions = {}
        self.board_upgrades = []
        self.reveled_actions = []
        self.hidden_actions = []

        pass


