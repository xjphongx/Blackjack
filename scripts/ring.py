import pygame
from scripts.button import Button

class Ring():
    def __init__(self,game,gameboard, x,y,order):
        self.game = game
        self.gameboard = gameboard
        self.x, self.y = x, y
        self.order = order
        hand_ring_image = pygame.image.load("images/hand_ring.png").convert_alpha() 
        self.button = Button(self.x, self.y, hand_ring_image,scale=.25)
        self.chip = None
        self.background_dot_image = pygame.image.load("images/background_dot.png").convert_alpha()
        

    def display(self):
        if self.button.draw(self.game.display):
            if self.button.isActive == False and self.game.player.bet_amount > 0:
                self.game.player.add_Hand(self.order) #add hand at position 1
                self.button.isActive = True #makes the button active once
                self.chip = self.gameboard.cursor.chip
                self.rect = self.chip.get_rect() #used to center the chip in ring
                self.rect.center = (self.x,self.y)
                #clear cursor
                self.gameboard.cursor.chip = None
                       
    def clear_hand(self):
        self.game.player.remove_Hand(self.order)
        self.button.isActive = False


    def update(self):
        if self.chip != None:
            self.game.display.blit(self.chip, (self.rect.x, self.rect.y))
        


