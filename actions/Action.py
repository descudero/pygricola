from pydispatch import dispatcher
from pygame.sprite import LayeredUpdates
from pygame.sprite import Sprite
import pygame


class Action:

    def __init__(self, name, cost, result, requirement):
        self.name = name
        self.cost = cost
        self.result = result
        self.requirement = requirement

    def do(self, player):
        player.use_resources(self.cost)
        dispatcher.send(signal="do", sender=self, player=player)
        return self.result

    def possible(self, player):
        for attr, resource_required in self.requirement.items():
            try:
                resource_level = getattr(player, attr)
                if resource_required > resource_level:
                    return False
            except AttributeError:
                return False
        else:
            return True

    def sprite(self, rect):
        action_sprite = Sprite()
        action_sprite.pygame.image.load("../images/" + self.__class__.__name__ + ".png").convert()
        action_sprite.rect = rect
        return action_sprite
