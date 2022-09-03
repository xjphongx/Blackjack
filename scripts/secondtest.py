from Stack import Stack ## from Stack.py file, import and use the Stack class
from Card import Card   ## from Card.py file, import and uses Card class
import json 


##testing area
testStack = Stack()
with open('cards.json') as jsonfile:
#jsonfile = open('cards.json')#another way to open
    card = json.load(jsonfile)
print(f"The is the amount of decks in this stack {card['amount_of_decks']}")
for data_item in card['card_decks']:
##create a new Card for every interation and push into stack
    card_Obj = Card(data_item['card_type'], data_item['pip_value'], data_item['suit'])
    testStack.push(card_Obj)
##ISSUE: ACES NEED TO HAVE DIFFERENT VALUES PUSHED INTO STACK

print("Updating stack size")
testStack.update_size()

print("Stack before cut")
for i in range(testStack.get_size()):
    print(testStack.stack[i].get_card_type(),end = " ")

print("Initializing cut()")
testStack.cut_deck()
#check out the shuffle cut list
for j in range(testStack.get_size()):
    print(testStack.stack[j].get_card_type(), end = " ")

print("\nIntializing casino_shuffle()")
testStack.casino_shuffle()
testStack.casino_shuffle()
testStack.casino_shuffle()
testStack.casino_shuffle()
for j in range(testStack.get_size()):
    print(testStack.stack[j].get_card_type(), end = " ")

jsonfile.close()
