from Hand import Hand

DEALER_STARTING_FUND = 99999999999999999999999999999999999999999
PLAYER_STARTING_FUND = 1000

class Player:
    def __init__(self, fund = PLAYER_STARTING_FUND):
        self.hand_list = Hand()
        self.fund = fund
        self.is_player_turn = False
        self.player_action = None

    def add_Hand(self):#Player can add a new hand when SPLITING
        hand = Hand()
        self.hand_list.append(hand)
    
    def add_funds(self, added_amount):
        self.fund += added_amount
    
    def subtract_funds(self, subtracted_amount):
        self.fund -= subtracted_amount

    def move_hand_to_discard(self):
        pass


    ####Player Actions: Hit, Stand, Split, Double
    def hit():
        pass
    def stand():
        pass
    def split():
        pass
    def double():
        pass

class Dealer(Player):
    def __init__(self, fund = DEALER_STARTING_FUND):
        super().__init__(fund)

