import pygame
from scripts.button import Button

class Ring():
    def __init__(self,game, x,y,order):
        self.game = game
        self.x, self.y = x, y
        self.order = order
        hand_ring_image = pygame.image.load("images/hand_ring.png").convert_alpha() 
        self.button = Button(self.x, self.y, hand_ring_image,scale=.25)

    def display(self):
        if self.button.draw(self.game.display):
            if self.button.isActive == False and self.game.player.bet_amount > 0:
                self.game.player.add_Hand(self.order) #add hand at position 1
                self.button.isActive = True #makes the button active once
                #TODO create a ring object for placement access
                #self.game.display.blit(self.cursor.last_chip, (self.hand_1_x,self.hand_1_y))
                



