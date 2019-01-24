from cards import *


class Card:
    def __init__(self):
        self.name = ""
        self.requirements = {}
        self.text = ""
        self.victory_points = 0
        self.complexity = 'S'

    @staticmethod
    def generate_deck(complexity=['S']):
        pass
