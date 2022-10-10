import pygame


class Cursor():
    def __init__(self, game):
        self.game = game
        #self.chip_stack = []
        
        self.last_chip = None

    def update(self):
        #update and blit the image at the cursors location
        x, y = pygame.mouse.get_pos()
        if(self.last_chip != None):
            self.game.display.blit(self.last_chip,(x,y))

