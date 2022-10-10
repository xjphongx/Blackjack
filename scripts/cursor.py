import pygame


class Cursor():
    def __init__(self, game):
        self.game = game
        #self.chip_stack = []
        
        self.chip = None
        #self.hasChip = False

    def update(self):
        #update and blit the image at the cursors location
        x, y = pygame.mouse.get_pos()
        if(self.chip != None):
            self.game.display.blit(self.chip,(x,y))

