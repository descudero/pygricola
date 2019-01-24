from Player import Player
from actions.BoardAction import GrainSeeds
from pydispatch import dispatcher


def handle_event(sender, player):
    """Simple event handler"""
    print('Signal was sent by', sender, player)
    player.add_results({"grain": 1})

player = Player(uid=1)

print(player.display_player())
gs = GrainSeeds()
gs2 = GrainSeeds()
dispatcher.connect(handle_event, signal="do", sender=gs)
for i in range(1):
    player.do(gs)
for i in range(1):
    player.do(gs2)
print(player.display_player())
