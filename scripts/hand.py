from scripts.placement import Placement
from scripts.action_menu import Action_Menu

class Hand():
    def __init__(self, game, gameboard, order, x, y, bet_amount = 0 , isDealer = False): #add bet size when creating a hand, minimum bet
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
                display.blit(card.card_back_surface, card.rect)
            else:
                display.blit(card.image_surface, card.rect)
        
    def display_result(self):
        if self.win_amount > 0:
            self.game.draw_text(f" + {self.win_amount}",20,self.x + 40, self.y + 100)
        if self.lost_amount > 0:
            self.game.draw_text(f" - {self.lost_amount}",20,self.x + 40, self.y + 100)

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
            self.hand_sum += card.low_pip_value
            self.hand_upper_sum += card.high_pip_value
        else:
            self.hand_sum += card.pip_value
            self.hand_upper_sum += card.pip_value
        self.card_list.append(card) 
        self.hand_size+=1       #increase hand size when adding a card
        
    def remove_card(self):
        self.hand_sum -= self.card_list[-1].pip_value
        temp_card = self.card_list.pop()
        self.hand_size = len(self.card_list) #update hand size after pop, to prevent error
        return temp_card
         


        
    
