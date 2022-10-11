import pygame
from scripts.button import Button

class Ring():
    def __init__(self,game,gameboard, x,y,order):
        self.game = game
        self.gameboard = gameboard
        self.x, self.y = x, y
        self.order = order #ring's given order from right to left
        hand_ring_image = pygame.image.load("images/hand_ring.png").convert_alpha() 
        self.button = Button(self.x, self.y, hand_ring_image,scale=.25)
        self.chip = None
        self.hasChip = False
        self.bet_amount = 0 #used to update with dealer
        
    #function display draws the ring image and adds functionality
    def display(self):
        if self.button.draw(self.game.display):
            #add hand if the ring is empty
            if self.button.isActive == False and self.game.player.current_bet > 0:
                self.game.player.add_Hand(self.order) #add hand at position 1
                self.button.isActive = True #makes the button active once
                self.chip = self.gameboard.cursor.chip
                self.rect = self.chip.get_rect() #used to center the chip in ring
                self.rect.center = (self.x,self.y)
                self.hasChip = True #ring has a chip inside
                self.gameboard.cursor.chip = None #resets the cursor to hold nothing

                #calculate and updates bet
                self.bet_amount += self.game.player.current_bet
                self.game.player.current_bet = 0
                
            #continuesly able to add bets when the hand is active
            elif self.game.player.current_bet > 0:
                self.chip = self.gameboard.cursor.chip
                self.gameboard.cursor.chip = None #resets the cursor to hold nothing
                #calculate and updates bet
                self.bet_amount += self.game.player.current_bet
                self.game.player.current_bet = 0
                
    #function clear resets the ring to default            
    def clear(self):
        self.chip = None
        self.hasChip = False
        self.button.isActive = False
        #update bet amounts
        self.game.player.fund += self.bet_amount
        self.bet_amount = 0

    #function update blits the chip onto and within the ring
    def update(self):
        #print(self.chip)
        if self.hasChip == True:
            self.game.draw_text(str(self.bet_amount),40, self.rect.x+45, self.rect.y-25)
            self.game.display.blit(self.chip, (self.rect.x, self.rect.y))
        


