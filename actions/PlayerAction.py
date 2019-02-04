from pydispatch import dispatcher
from pygame.sprite import LayeredUpdates
from pygame.sprite import Sprite
import pygame


class PlayerAction(LayeredUpdates):
    width = 60
    height = 120

    def __init__(self, action, player_actions, index):
        self.player_actions = player_actions
        self.action = action
        self.index = index
        self.x = self.player_actions.x + self.index * PlayerAction.width
        self.y = self.player_actions.y
        self.rect = pygame.Rect((self.x, self.y), (PlayerAction.width, PlayerAction.height))
        action_sprite = action.sprite(self.rect)
        action_sprite._layer = 0
        self.marked = False
        self.selected = False
        self.add(action_sprite)

    def mark(self):
        pass
