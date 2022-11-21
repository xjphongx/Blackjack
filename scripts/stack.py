import random,math,pygame,os,json
from scripts.card import Card



#Stack Data Structure Class
#@Parameters: (None)
#Class variables contain a stack as a list and stack size as an Int    
class Stack():
    ## predefined functions for list: append(),pop()
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self,value):           #adds to the end of the list
        self.stack.append(value)
        self.size +=1
    def pop(self):                  #removes the object at the end of the list
        self.stack.pop()
        self.size = len(self.stack)
    def top(self):                  #returns the end of the list 
        return self.stack[-1]
    def show(self):                 #print the list of card type
        for i, card in enumerate(self.stack) :
            print(card.type, end= " ")  
        print() #skips a line
    def clear(self):
        self.stack = []
        self.size = 0
    def get_size(self):             #return length of the list
        return len(self.stack)
    def update_size(self):          #update class size with its current list size
        self.size = len(self.stack)
        #i might not need this if i update after every pop
    #add a get top 10 
    
class DeckPile(Stack,pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_path = os.path.abspath('images/PNG_cards/card_back.png')
        self.image_surface = pygame.image.load(self.image_path).convert_alpha()
        self.image_surface = pygame.transform.rotozoom(self.image_surface,0,.2)
        self.rect = self.image_surface.get_rect(center = (1225,80))
        
    #load json png cards into the deck
    def load_cards_to_deck(self):
        CARD_PATH_TO_JSON = 'scripts/cards.json'
        with open(CARD_PATH_TO_JSON, 'r') as jsonfile: #opens the cards json file
            cards = json.load(jsonfile)
        #creates 6 decks of cards in one pile
        for i in range(6): #TODO is there anyway to make loading faster?
            for data_item in cards['card_decks']:
                #create a new card for every iteration
                card_object = Card(
                    data_item['type'],
                    data_item['pip_value'],
                    data_item['suit'],
                    data_item['card_image'],
                    cards['card_back_image']
                )#end of card_object
                self.stack.append(card_object)#push the card object into gameboard's deck_pile
                self.size += 1 #update size after adding card

        jsonfile.close() #close the json file
    
    #Function cut_deck() contains 3 steps:
    #   Step 1: Identify the 40% to 60% mark and split accordingly
    #   Step 2: Places the top and bottom portion into a temporary container, respectively
    #   Step 3: Set class stack to be the temporary container
    #Text Representation:
    #   Before cut_deck(): [   bottom    ][   top     ]  <- top of stack
    #   After cut_deck():  [   top     ][   bottom    ]  <- top of stack
    def cut_deck(self):
        tempList = []   #temporary container
        ##40% - 60% cut so it cuts randomly
        cut_limit = random.randint(int(math.ceil(.4*self.size)), int(math.ceil(.6*self.size)))
        for i in range(cut_limit,self.size): #moves the top portion into temp
            tempList.append(self.stack[i])
        for j in range(0,cut_limit):
            tempList.append(self.stack[j])   #moves the bottom portion into temp
        self.stack = tempList.copy()         #updates the class stack to the resulting temp list
        #print(self.stack)

    #Function casino_shuffle() contains three steps:
    #   Step 1: Split the stack into two equal halves
    #   Step 2: Alternately append the two list into a shuffled list
    #   Step 3: Set the class stack to be the shuffled list
    def casino_shuffle(self):
        tempList = [] 
        for i in range(int(self.size/2), self.size): #put upper half of object's stack into tempList
            tempList.append(self.stack[i])    
        for j in range(int(self.size/2), self.size): #pop the objects that were appended previously
            self.stack.pop()
        #Alternately shuffle the two list into a shuffled list
        shuffledList= []
        for k in range(int(self.size/2)): #loop through half the original size
            try: #try to pop the bottom objects into the shuffled list
                shuffledList.append(self.stack.pop(0))
                shuffledList.append(tempList.pop(0))
            except IndexError:
                print("Index error when casino shuffling")
                break   
        self.stack = shuffledList[:]    #updates the class stack

    #Function combine():
    #   Purpose is to join together the two stack object's stack list data structure
    #   and clear the discard pile's stack
    def combine(self, discard_pile: Stack):
        self.stack.extend(discard_pile.stack)
        discard_pile.clear()

class DiscardPile(Stack,pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_path = os.path.abspath('images/discard_pile.png')
        self.image_surface = pygame.image.load(self.image_path).convert_alpha()
        self.image_surface = pygame.transform.rotozoom(self.image_surface,0,.4)
        self.rect = self.image_surface.get_rect(center = (80,100))


   
