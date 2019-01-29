from pydispatch import dispatcher


class Farm:
    def __init__(self, player, board):
        self.spaces = []
        self.rooms = []
        self.fields = []
        self.fences = []
        self.barns = []
        self.player = player
        self.shape = (3, 5)
        self.house_level = 0
        self.board = board

    def sow(self, field, crop):
        vegetables = True if crop == "vegetables" else False
        grain = True if crop == "grain" else False
        field.sow(grain=grain, vegetables=vegetables)

    def plow(self, x, y):
        self.fields.append(Field(x=x, y=y, farm=self))


class SingleSpace:
    def __init__(self, x, y, farm):
        self.x = x
        self.y = y
        self.farm = farm


class Field(SingleSpace):
    def __init__(self, x, y, farm):
        super().__init__(x=x, y=y, farm=farm)
        self.grain = 0
        self.vegetables = 0
        dispatcher.connect(receiver=self.harvest, signal="harvest", sender=farm.board)

    def sow(self, grain=False, vegetables=False):
        if self.grain == 0 and self.vegetables == 0:
            if (grain):
                self.grain = 3
            elif vegetables:
                self.vegetables = 2

    def harvest(self):

        self.farm.player.add_results({"grain": self.grain, "vegetables": self.vegetables})
        self.vegetables = 0
        self.grain = 0


class MultiSpace:
    pass
