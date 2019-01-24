import unittest
from Player import Player
from Player import NotEnoughResourcesException
from actions.BoardAction import GrainSeeds


class TestPlayer(unittest.TestCase):

    def test_add_clay(self):
        resources = {"clay": 1}
        player = Player(uid=1)
        player.add_results(resources)
        self.assertTrue((player.clay == 1))

    def test_add_wood(self):
        resources = {"wood": 1}
        player = Player(uid=1)
        player.add_results(resources)
        self.assertTrue((player.wood == 1))

    def test_add_grain(self):
        resources = {"grain": 1}
        player = Player(uid=1)
        player.add_results(resources)
        self.assertTrue((player.grain == 1))

    def test_use_resources_exception(self):
        resources = {"grain": 1}
        player = Player(uid=1)
        with self.assertRaises(Exception) as context:
            player.use_resources(resources)

        self.assertTrue('Not Enough Resources ' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
