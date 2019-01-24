from PlayerFarm import PlayerFarm


class NotEnoughResourcesException(Exception):
    pass


class Player:
    def __init__(self, uid):
        self.uid = uid
        self.wood = 0
        self.food = 0
        self.stone = 0
        self.reed = 0
        self.grain = 0
        self.clay = 0

        self.vegetables = 0

        self.family_members = 2
        self.sheep = 0
        self.cow = 0
        self.pig = 0

        self.rooms = 0
        self.farm = PlayerFarm(self)

        self.acquired_upgrades = {}
        self.acquired_jobs = {}

        self.job_cards = {}
        self.upgrade_cards = {}
        self.player_actions = {}
        self.used_family_member = 0

    def do(self, action):
        self.add_results(action.do(self))

    def add_results(self, results):
        for attr, value in results.items():

            if hasattr(self, attr):
                setattr(self, attr, getattr(self, attr) + value)

    def display_player(self):
        string = "Player {no} grain {grain} ".format(no=self.uid, grain=self.grain)

        return string

    def use_resources(self, cost):
        for attr, value in cost.items():

            if hasattr(self, attr):
                if value > getattr(self, attr):
                    raise NotEnoughResourcesException(" Not Enough Resources {resource}  Actual {actual} Cost {cost}"
                                                      .format(resource=attr, actual=getattr(self, attr), cost=value))
                else:
                    setattr(self, attr, getattr(self, attr) - value)
