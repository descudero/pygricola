from pydispatch import dispatcher
from pygame.sprite import LayeredUpdates
from pygame.sprite import Sprite
import pygame


class PossiblePlayerActions:

    def __init__(self, player):
        self.x = 0
        self.y = 500
        self.player = player
        self.active_actions = []

    def __iter__(self):
        return iter(self.active_actions)

    def add_action(self, action):
        self.active_actions.append(action)

    @property
    def possible_actions(self):
        return [action for action in self if action.possible(self.player)]
