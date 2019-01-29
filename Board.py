from pydispatch import dispatcher

class Board:
    def __init__(self, number_players=2):
        self.board_actions = {}
        self.board_upgrades = []
        self.reveled_actions = []
        self.hidden_actions = []

        pass

    def upkeep(self):
        dispatcher.send(signal="upkeep", sender=self)

    def end(self):
        dispatcher.send(signal="end", sender=self)
