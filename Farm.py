from pydispatch import dispatcher
from pygame.sprite import LayeredUpdates
from pygame.sprite import Sprite
import pygame


class Farm:
    def __init__(self, player, board):
        self.x = 1000
        self.y = 0
        self.slots = []
        self.slots = [FarmSlot(x, y, self) for x in range(0, 5) for y in range(0, 3)]
        self.slots[0].build("WoodRoom")
        self.slots[1].build("WoodRoom")
        self.fences = []
        self.barns = []
        self.player = player
        self.house_level = "Wood"
        self.board = board

    def sow(self, field, crop):
        vegetables = True if crop == "vegetables" else False
        grain = True if crop == "grain" else False
        field.sow(grain=grain, vegetables=vegetables)

    def plow(self, x, y):
        self.fields.append(Field(x=x, y=y, farm=self))

    def draw(self, surface):
        for slot in self.slots:
            slot.draw(surface=surface)

    def get_single_spaces(self, ):
        pass

    def get_slots_at(self, pos):
        for slot in self:
            if slot.get_sprites_at(pos):
                return slot
        else:
            return 0

    def farm_slots(self, type_farmslot):
        return [slot for slot in self if slot._is == type_farmslot]

    def __iter__(self):
        return iter(self.slots)

    @property
    def fields(self):
        return self.farm_slots(type_farmslot="Field")

    @property
    def free_spaces(self):
        return self.farm_slots(type_farmslot="FreeSpace")

    @property
    def rooms(self):
        return self.farm_slots(type_farmslot=self.house_level + "Room")

    @property
    def marked(self):
        return [slot for slot in self if slot.marked]

    @property
    def selected(self):
        return [slot for slot in self if slot.selected]

    def has_selected(self):
        return len(self.selected) > 0

    def has_selected(self):
        return len(self.marked) > 0


class FarmSlot(LayeredUpdates):
    width = 160
    height = 160

    def __init__(self, farm_x, farm_y, farm):
        self.farm_x = farm_x
        self.farm_y = farm_y
        self.x = (farm_x * FarmSlot.width) + farm.x
        self.y = (farm_y * FarmSlot.height) + farm.y
        self.farm = farm
        self.rect = pygame.Rect((self.x, self.y), (FarmSlot.width, FarmSlot.height))
        self.selected = False
        self.marked = False

        super().__init__(FreeSpace(slot=self))

    def build(self, class_building):
        self.remove_sprites_of_layer(layer_nr=0)
        self.add(eval(class_building)(slot=self))

    def is_type(self, class_building):
        low_sprints = self.get_sprites_from_layer(layer=0)[0]
        return isinstance(low_sprints, eval(class_building))

    def mark(self):
        self.marked = True
        mark = Sprite()
        mark.image = pygame.image.load("images/Mark.png").convert_alpha()
        mark.rect = self.rect
        mark._layer = 4
        self.add(mark)

    def un_mark(self):
        self.marked = True
        self.remove_sprites_of_layer(layer_nr=4)

    def un_select(self):
        self.selected = False
        self.remove_sprites_of_layer(layer_nr=5)

    def select(self):
        self.selected = True
        select = Sprite()
        select.image = pygame.image.load("images/Selected.png").convert_alpha()
        select.rect = self.rect
        select._layer = 5
        self.add(select)

    @property
    def _is(self):
        return self.get_sprites_from_layer(layer=0)[0].__class__.__name__


class SingleSpace(Sprite):
    def __init__(self, slot, layer):
        self._layer = layer
        self.slot = slot

        self.rect = slot.rect
        self.image = pygame.image.load("images/" + self.__class__.__name__ + ".png").convert()
        super().__init__()


class FreeSpace(SingleSpace):
    def __init__(self, slot):
        super().__init__(slot=slot, layer=0)


class WoodRoom(SingleSpace):
    def __init__(self, slot):
        super().__init__(slot=slot, layer=0)

    def upgrade(self, next_level="ClayRoom"):
        self.slot.build(class_building=next_level)


class ClayRoom(WoodRoom):
    def __init__(self, slot):
        super().__init__(slot=slot, layer=0)

    def upgrade(self, next_level="StoneRoom"):
        super().upgrade(next_level=next_level)


class StoneRoom(ClayRoom):
    def __init__(self, slot):
        super().__init__(slot=slot, layer=0)

    def upgrade(self, next_level=""):
        pass


class Field(SingleSpace):
    def __init__(self, slot):
        super().__init__(slot=slot)
        self.grain = 0
        self.vegetables = 0
        dispatcher.connect(receiver=self.harvest, signal="harvest", sender=self.slot.farm.board.game)

    def sow(self, grain=False, vegetables=False):
        if self.grain == 0 and self.vegetables == 0:
            if grain:
                self.grain = 3
            elif vegetables:
                self.vegetables = 2

    def harvest(self):

        self.farm.player.add_results({"grain": self.grain, "vegetables": self.vegetables})
        self.vegetables = 0
        self.grain = 0


class MultiSpace:
    pass
