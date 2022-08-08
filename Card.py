from Stack import Stack ## from Stack.py file, import and use the Stack class
import json
class Card:

    def __init__(self, card_type,pip_value, suit):
        self.card_type = card_type
        self.pip_value = pip_value
        self.suit = suit
        self.low_pip_value=0        #used for Aces
        self.high_pip_value=0       #used for Aces
        ##self.value = 0 ## this will change 











## testing area
testCard = Card(5,"Spade")
testStack = Stack()
testStack.push(1)
testStack.push(2)
testStack.push(3)
print(testStack.top())