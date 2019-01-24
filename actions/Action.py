class Action:
    def __init__(self, name, cost, result, requirement):
        self.name = name
        self.cost = cost
        self.result = result
        self.requirement = requirement

    def do(self, player):
        print(self.result)
        player.use_resources(self.cost)
        return self.result
