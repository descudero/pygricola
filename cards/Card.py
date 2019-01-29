from cards import *


class Card:
    def __init__(self, name, requirements, text, victory_points, complexity='S'):
        self.name = name
        self.requirements = requirements
        self.text = text
        self.victory_points = victory_points
        self.complexity = complexity

    @staticmethod
    def generate_deck(complexity=['S']):
        pass


class Occupation(Card):
    def __init__(self, name, requirements, text, victory_points, complexity='S'):
        super().__init__(name=name, requirements=requirements, text=text, victory_points=victory_points,
                         complexity=complexity)

    def play(self, player):
        player.add_occupation(self)

    def check_requirements(self, player):

        for attr, required_level in self.requirements.items():
            if getattr(player, attr) < required_level:
                return False
        else:
            return True
