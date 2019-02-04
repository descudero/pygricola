class UI:
    def __init__(self, game):
        self.game = game


class CliUI(UI):
    def __init__(self, game):
        super().__init__(game=game)

    def show_board(self):
        pass

    def show_player_farm(self, player):
        pass

    def show_player_resources(self, player):
        pass

    def get_board_action(self, index_board):
        pass

    def show_player_actions(self, player):
        pass
