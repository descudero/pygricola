from Player import Player
from Board import Board
from pydispatch import dispatcher
from UI import CliUI
import pygame


class Game:
    def __init__(self, number_players=1):
        pygame.init()
        width = 1800
        height = 1000
        self.screen = pygame.display.set_mode((width, height))

        self.board = Board(number_players=number_players, game=self)
        self.players = [Player(uid=uid, game=self) for uid in range(0, number_players)]
        self.active_player = self.players[0]

        self.ui = CliUI(game=self)

    def upkeep(self):
        dispatcher.send(signal="upkeep", sender=self)

    def end(self):
        dispatcher.send(signal="end", sender=self)

    def draw(self):
        self.active_player.farm.draw(surface=self.screen)
        pygame.display.flip()

    def game_loop(self):
        white = (255, 255, 255)
        self.screen.fill(white)
        running = True
        self.draw()
        pygame.display.flip()
        while running:
            self.screen.fill(white)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        slot = self.players[0].farm.get_slots_at(event.pos)
                        if slot._is() == "FreeSpace":
                            pygame.display.flip()
                            slot.build("WoodRoom")
                            self.draw()
                            pygame.display.flip()
                    except:
                        pass
                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    rect = redSquare.get_rect()
                    print(x,y,repr(redSquare),rect.x,rect.y,rect)
                    if redSquare.get_rect().collidepoint(x, y):
                        print('clicked on image',repr(redSquare))
                '''
        # loop over, quite pygame
        pygame.quit()


game = Game()

game.game_loop()
