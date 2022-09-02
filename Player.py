from Hand import Hand


class Player:
    def __init__(self):
        self.hand_list = Hand()
        self.fund = 0

    def add_Hand(self):#Player can addS a new hand when SPLITING
        hand = Hand()
        self.hand_list.append(hand)
    
    def add_funds(self, fund_ammount):
        self.fund += fund_ammount



    ####Player Actions: Hit, Stand, Split, Double
    def hit():
        pass
    def stand():
        pass
    def split():
        pass
    def double():
        pass