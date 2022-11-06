import pygame
from scripts.button import Button

class Ring():
    def __init__(self,game,gameboard, x,y,order):
        self.game = game
        self.gameboard = gameboard
        self.OFFSET = 175 #the distance from center of ring to the card placement
        self.x, self.y = x, y
        self.order = order #ring's given order from right to left
        self.hand_ring_image = pygame.image.load("images/hand_ring.png").convert_alpha() 
        self.rect = self.hand_ring_image.get_rect(center = (self.x,self.y))
        self.button = Button(self.x, self.y, self.hand_ring_image,scale=.25)
        self.chip = None
        self.hasChip = False
        self.bet_amount = 0 #used to update with dealer
        self.isValidBet = False
        
        
    #function display draws the ring image and adds functionality
    def display(self):
        if self.button.draw(self.game.display):
            #add hand if the ring is empty
            if self.button.isActive == False and self.gameboard.player.current_bet > 0:
                self.gameboard.player.add_Hand(self.order,self.x,self.y - self.OFFSET) #add hand at position 1
                self.button.isActive = True #makes the button active once
                self.chip = self.gameboard.cursor.chip
                self.rect = self.chip.get_rect() #used to center the chip in ring
                self.rect.center = (self.x,self.y)
                self.hasChip = True #ring has a chip inside
                self.gameboard.ring_row.isEmpty = False #once a hand is filled, the row cotains a hand
                self.gameboard.cursor.chip = None #resets the cursor to hold nothing

                #calculate and updates bet
                self.bet_amount += self.gameboard.player.current_bet
                self.gameboard.player.current_bet = 0 #reset current bet
                
            #continuesly able to add bets when the hand is active
            elif self.gameboard.player.current_bet > 0:
                self.chip = self.gameboard.cursor.chip
                self.gameboard.cursor.chip = None #resets the cursor to hold nothing
                #calculate and updates bet
                self.bet_amount += self.gameboard.player.current_bet
                self.gameboard.player.current_bet = 0
            
            #check if current ring bet is valid to game's minimum bet
            self.isValidBet = self.check_bet()
                
    #function clear resets the ring to default            
    def clear(self):
        self.chip = None
        self.hasChip = False
        self.button.isActive = False #Resets the button
        self.gameboard.ring_row.isEmpty = True #row is empty
        self.isValidBet = False #not a valid bet anymore 
        #update bet amounts
        self.gameboard.player.fund += self.bet_amount
        self.bet_amount = 0

    #function update blits the chip onto and within the ring
    def update(self):
        #print(self.chip)
        if self.hasChip == True:
            self.game.draw_text(str(self.bet_amount),40, self.rect.x+115, self.rect.y+80)
            self.game.display.blit(self.chip, (self.rect.x, self.rect.y))
        
        
    def check_bet(self) -> bool:
        if self.bet_amount < self.gameboard.min_bet:
            return False
        else:
            return True

