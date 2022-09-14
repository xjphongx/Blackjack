
class Hand:
    def __init__(self): #add bet size when creating a hand, minimum bet
        self.card_list = []
        self.bet_size = 50
        self.hand_sum = 0
        self.hand_upper_sum = 0 #calculated for ace egde case
        self.hand_size = 0
        self.player_action_menu = [] #LOOK AT TUTORIAL
        #need to add a small menu containing buttons for player to press 
    
    #print out on terminal the contains of the card_list
    def show(self):
        for i, card in enumerate(self.card_list) :
            print(card.type)    
    
    #update hand after every removal of a card to prevent index error
    def update_hand(self):
        self.hand_size = len(self.card_list)

    #reset hand total sum to zero
    def reset_hand_sum(self):
        self.hand_sum = 0

    #when adding cards to my hand, add pip value as well
    def add_card(self, card): 
        #set hand_sum to be the lower sum and hand uppper is uppper sum
        if card.type == 'Ace':
            self.hand_sum += card.low_pip_value
            self.hand_upper_sum += card.high_pip_value
        else:
            self.hand_sum = card.pip_value
            self.hand_upper_sum = card.pip_value

        self.card_list.append(card) 
        self.hand_size+=1       #increase hand size when adding a card
        

    def remove_card(self):
        #print(f"testing: {self.card_in_hand_list[-1]}")
        self.hand_sum -= self.card_list[-1].pip_value
        return self.card_list.pop()
         #Note: After every removal, call update_hand() to prevent index error


        
    
