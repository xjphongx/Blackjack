from Stack import Stack ## from Stack.py file, import and use the Stack class
import json ##doing my testing in Card.py file
class Card:

    def __init__(self, card_type, pip_value, suit):
        self.card_type = card_type
        self.pip_value = pip_value
        self.suit = suit
        if(card_type) == "Ace":
            self.low_pip_value=1         #used for Aces
            self.high_pip_value=11       #used for Aces
        
    def get_card_type(self):
        return self.card_type





## testing area
testCard = Card("Five", 5,"Spade")
testStack = Stack()


##Python loading json 
f = open('cards.json')
card = json.load(f)
print(f"The is the amount of decks in this stack {card['amount_of_decks']}")
##print(card['card_decks'])
for data_item in card['card_decks']:
    ##create a new Card for every interation and push into stack
    card_Obj = Card(data_item['card_type'], data_item['pip_value'], data_item['suit'])
    testStack.push(card_Obj)
    ##print(card_Obj)

##print(testStack.show())
print(testStack.top().get_card_type())
testStack.pop()
testStack.pop()
testStack.pop()
testStack.pop()
print(testStack.top().get_card_type())



f.close()