from actions.Action import Action
from pydispatch import dispatcher
from collections import Counter


class OccupiedBoarActionException(Exception):
    pass


class NoFamilyMembersException(Exception):
    pass


class BoardAction(Action):
    def __init__(self, name, cost, result, requirement, board):
        self.board = board
        self.used = False
        super().__init__(name, cost, result, requirement)
        dispatcher.connect(receiver=self.end, sender=self.board.game, signal="end")

    def end(self):
        self.used = False

    def do(self, player, number_times):
        if player.used_family_member == player.family_members:
            raise NoFamilyMembersException("No Family member")
        if self.used:
            raise OccupiedBoarActionException("Action Occupied")
        self.used = True
        return super().do(player)


class GrainSeeds(BoardAction):
    def __init__(self, board):
        super().__init__(name="Grain Seeds", cost={}, result={"grain": 1}, requirement={}, board=board)

    def do(self, player):
        self.player = player
        return super().do(player=player, number_times=1)


class DayLaborer(BoardAction):
    def __init__(self, board):
        super().__init__(name="Day Laborer", cost={}, result={"food": 2}, requirement={}, board=board)


class VegetablesSeeds(BoardAction):
    def __init__(self, board):
        super().__init__(name="Vegetables Seeds", cost={}, result={"vegetables": 1}, requirement={}, board=board)


class AccumulativeBoardAction(BoardAction):
    def __init__(self, name, cost, result, requirement, board, inc_resources={}):
        super().__init__(name=name, cost=cost, result=result, requirement=requirement, board=board)
        self.inc_resources = inc_resources
        dispatcher.connect(signal="upkeep", receiver=self.accumulate, sender=self.board.game)

    def accumulate(self):
        self.result = dict(Counter(self.result) + Counter(self.inc_resources))

    def do(self, player):
        result = super().do(player=player, number_times=1)
        self.result = {}
        return result


class ClayPit(AccumulativeBoardAction):
    def __init__(self, board):
        super().__init__(name="Clay Pit", cost={}, result={}, requirement={}, board=board, inc_resources={"clay": 1})


class ReedBank(AccumulativeBoardAction):
    def __init__(self, board):
        super().__init__(name="Reed Bank", cost={}, result={}, requirement={}, board=board, inc_resources={"reed": 1})


class FishingPond(AccumulativeBoardAction):
    def __init__(self, board):
        super().__init__(name="Fishing Pond", cost={}, result={}, requirement={}, board=board,
                         inc_resources={"food": 1})


class Forest(AccumulativeBoardAction):
    def __init__(self, board):
        super().__init__(name="Forest", cost={}, result={}, requirement={}, board=board, inc_resources={"wood": 3})


class WesternQuarry(AccumulativeBoardAction):
    def __init__(self, board):
        super().__init__(name="Western Quarry", cost={}, result={}, requirement={}, board=board,
                         inc_resources={"stone": 1})


class EasternQuarry(AccumulativeBoardAction):
    def __init__(self, board):
        super().__init__(name="Eastern Quarry", cost={}, result={}, requirement={}, board=board,
                         inc_resources={"stone": 1})


class PigMarket(AccumulativeBoardAction):
    def __init__(self, board):
        super().__init__(name="Pig Market", cost={}, result={}, requirement={}, board=board,
                         inc_resources={"pig": 1})


class SheepMarket(AccumulativeBoardAction):
    def __init__(self, board):
        super().__init__(name="Sheep Market", cost={}, result={}, requirement={}, board=board,
                         inc_resources={"sheep": 1})


class CatleMarket(AccumulativeBoardAction):
    def __init__(self, board):
        super().__init__(name="Catle Market", cost={}, result={}, requirement={}, board=board,
                         inc_resources={"catle": 1})


class Lessons(BoardAction):
    def __init__(self, board):
        super().__init__(name="Lessons", cost={"food": 1}, result={"": 0}, requirement={}, board=board)

    def do(self, player, occupation):
        if player.occupations == 1:
            self.cost = 1
        super().do(player, number_times=1)
        occupation.play(player=player)


class Plow(BoardAction):
    def __init__(self, board):
        super().__init__(name="Plow", cost={}, result={"": 0}, requirement={}, board=board)

    def do(self, player, slot):
        player.farm.build("Field")


class Sow(BoardAction):
    def __init__(self, board):
        super().__init__(name="Sow", cost={}, result={"": 0}, requirement={}, board=board)

    def do(self, player, slot, crop):
        player.farm.sow(slot, crop)

        player.use_resources(cost={crop: 1})
