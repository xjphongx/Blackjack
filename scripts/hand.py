from scripts.placement import Placement
from scripts.action_menu import Action_Menu
from scripts.card import Card

class Hand():
    def __init__(self, game, gameboard, order, x, y, bet_amount = 0 , isDealer = False, isExtra=False): #add bet size when creating a hand, minimum bet
        self.game = game #reference to the game
        self.gameboard = gameboard #reference to the gameboard
        self.order = order #the hand's order
        self.x, self.y = x, y
        self.placement = Placement(x,y)
        self.isDealer = isDealer
        self.card_list = []
        self.min_bet = 50
        self.bet_amount = bet_amount
        self.win_amount = 0
        self.lost_amount = 0
        self.hasAce = False
        self.hand_sum = 0
        self.hand_upper_sum = 0 #calculated for ace edge case
        self.hand_size = 0
        self.isTurn = False
        self.action_menu = Action_Menu(self, self.game,self.gameboard, self.x, self.y)  #pass itself by reference
        self.isExtra = isExtra #used to identify extra hands for deleting memory
        self.hasChip = False
        self.chip = None
        self.chip_x = None
        self.chip_y = None
        self.bust = False
        self.stand = False
    #function display updates the pygame game display with cards
    def display(self, display):
        if not self.isDealer:
            #display the bet amount for THAT hand
            self.game.draw_text(f"Bet: {self.bet_amount}", 30, self.x, self.y + 120)
            self.display_result()
           
        for i, card in enumerate(self.card_list):
            #if card is faced down
            if card.isFaceDown:
                display.blit(card.card_back_surface, (card.rect.x,card.rect.y))
            else:
                display.blit(card.image_surface, (card.rect.x,card.rect.y))
        
        #display the new hand's chip next
        if self.hasChip:
            display.blit(self.chip,(self.chip_x,self.chip_y))

    def reset_hand(self):
        self.card_list = []
        self.win_amount = 0
        self.lost_amount = 0
        self.hand_sum = 0
        self.hand_upper_sum = 0
        self.hand_size = 0
        self.hasAce = False
        self.isTurn = False
        self.bust = False
        self.stand = False
        self.placement.x = self.x
        self.placement.y = self.y
        self.action_menu.reset_placement()
    
    def display_result(self):
        if self.win_amount > 0:
            self.game.draw_text(f" + {self.win_amount}",20,self.x + 40, self.y + 100)
        if self.lost_amount < 0:
            self.game.draw_text(f"{self.lost_amount}",20,self.x + 40, self.y + 100)

    #print out on terminal the contains of the card_list
    def show(self):
        for i, card in enumerate(self.card_list) :
            print(card.type, end= " ")  
        print()  
    
    #reset hand total sum to zero
    def reset_hand_sum(self):
        self.hand_sum = 0

    #when adding cards to my hand, add pip value as well
    def add_card(self, card): 
        #set hand_sum to be the lower sum and hand uppper is uppper sum
        if card.type == 'Ace':
            self.hasAce = True
            self.hand_sum += card.pip_value
            self.hand_upper_sum += card.high_pip_value
        else:
            self.hand_sum += card.pip_value
            self.hand_upper_sum += card.pip_value
        self.card_list.append(card) 
        self.hand_size+=1       #increase hand size when adding a card
    
    #Function remove_card pops the top of hand's card list 
    def remove_card(self)-> Card:
        
        if self.card_list[-1].type == 'Ace':
            if self.card_list[0].type == 'Ace':
                self.hasAce = True 
            else:
                self.hasAce = False #set to false if botton card is not an ace
            self.hand_sum -= self.card_list[-1].pip_value
            self.hand_upper_sum -= self.card_list[-1].high_pip_value
        else:
            self.hand_sum -= self.card_list[-1].pip_value
            self.hand_upper_sum -= self.card_list[-1].pip_value
        
        temp_card = self.card_list.pop()
        self.hand_size = len(self.card_list) #update hand size after pop, to prevent error
        return temp_card
         


        
    
