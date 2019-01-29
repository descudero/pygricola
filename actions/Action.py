from pydispatch import dispatcher

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
