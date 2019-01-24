from actions.Action import Action


class OccupiedBoarActionException(Exception):
    pass


class NoFamilyMembersException(Exception):
    pass


class BoardAction(Action):
    def __init__(self, name, cost, result, requirement):
        self.used = False
        super().__init__(name, cost, result, requirement)

    def do(self, player, number_times):
        if player.used_family_member == player.family_members:
            raise NoFamilyMembersException("No Family member")
        if self.used:
            raise OccupiedBoarActionException("Action Occupied")
        self.used = True
        return super().do(player)


class GrainSeeds(BoardAction):
    def __init__(self):
        super().__init__(name="Grain Seeds", cost={}, result={"grain": 1}, requirement={})

    def do(self, player):
        return super().do(player=player, number_times=1)
