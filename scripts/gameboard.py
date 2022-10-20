
import pygame, math, time
from scripts.bet_menu import Bet_Menu
from scripts.cursor import Cursor
from scripts.hand import Hand
from scripts.player import Dealer, Player
from scripts.ring_row import Ring_Row
from scripts.stack import DeckPile, DiscardPile
from scripts.state import State
from scripts.button import Button

class Gameboard(State):
    def __init__(self, game):
        super().__init__(game)
        #instantiating gameboard objects
        self.playing = False
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(325, 50, back_image, self.game.IMAGE_SCALE)
        self.dealer = Dealer()
        self.deck_pile = DeckPile()
        self.deck_pile.load_cards_to_deck()
        self.discard_pile = DiscardPile()
        for i in range(8):     #shuffle the deck when starting the gameboard
            self.deck_pile.cut_deck()
            self.deck_pile.casino_shuffle()          
        #temporary button
        confirm_button_image = pygame.image.load("images/buttons/confirm_button.png").convert_alpha()
        self.confirm_button = Button(self.game.display_width/2, self.game.display_height/2, confirm_button_image,scale=.1)
        
        self.ring_row = Ring_Row(self.game, self)
        self.bet_menu = Bet_Menu(self.game, self) 
        self.cursor = Cursor(self.game) 
        self.player = Player()
        self.turn_list = []

        self.current_time = 0
        self.static_time = 0
        
    def render(self,display):
        display.fill(self.game.background_color)
        #set up dealer
        self.game.draw_text("Dealer", 30, self.game.display_width/2,125)
        self.game.display.blit(self.dealer.dealer_image_surface, self.dealer.rect)           
        #set up deck
        self.game.display.blit(self.deck_pile.deck_back_image_surface, self.deck_pile.rect) 
        #set up discard pile
        self.game.display.blit(self.discard_pile.discard_pile_image_surface, self.discard_pile.rect)       
        #betting bar and functionality
        self.bet_menu.display()
        #hand ring functionality
        self.ring_row.display()

        if self.playing:
            #Start the game
            #display the cards from each hand
            for i, hand in enumerate(self.turn_list):
                hand.display(self.game.display)
        else:
            self.game.draw_text("How many hands are you playing?", 50, self.game.display_width/2,self.game.display_height/5)

        #checks if player is deciding, if clicked, pass out cards
        if self.confirm_button.isActive == False: 
                
                #if player clicks the confirm button and the row is empty, do nothing
                if self.ring_row.isEmpty == True :
                    self.confirm_button.draw(self.game.display) #still display the button
                    
                #if player places a bet, confirm and play the game
                elif self.ring_row.isEmpty == False: 
                    if self.confirm_button.draw(self.game.display): #figure out how to clear this button
                        
                        #combine the player and dealer hands, player goes first
                        self.turn_list.extend(self.dealer.hand_list)
                        self.turn_list.extend(self.player.hand_list)
                        self.turn_list.reverse() #makes sure the player is dealt cards first
                        self.confirm_button.isActive = True #removes the confirm button from screen
                        #self.game.display.blit(self.hand_1_button.image,(self.confirm_button.rect.x,self.confirm_button.rect.y))
                        #print(f"Player's Hand {self.player.hand_list}")
                        #print(f"Dealer's Hand {self.dealer.hand_list}")
                        #print(f"Turn list {self.turn_list}")

                        self.filter_List()
                        #print(f"After filter Turn list {self.turn_list}")

                        #pass out cards and start the blackjack game
                    
                        self.pass_cards()
                        self.playing = True


        #render the clickable button
        if self.back_button.draw(self.game.display):
            self.ring_row.clear() #clears the row 
            self.game.actions["back"] = True

    #state change to the title
    def update(self,actions):
        if actions["back"]:
            self.exit_state()
        self.game.reset_actions()

    #function filter list uses a simple algorithm to search and replace the list
    def filter_List(self):
        temp_list = []   #temperary list to contain hand objects     
        for i, hand in enumerate(self.turn_list): #cycles and gets the hand 
            if isinstance(hand, Hand): #test if hand is a hand object
                temp_list.append(hand)

        self.turn_list = temp_list.copy() #turn list is replaced with the filtered lsit
        temp_list.clear()
        



    def pass_cards(self):
        print(self.turn_list)
        #intial passing of cards to each hand and dealer, only passes out 2 cards
        #this algorithm passes out cards in circle order from hand 1 - 5 and dealer's hand
        for rotation in range(2):
            for i, hand in enumerate(self.turn_list):
                #add the top card into the hand in turn list
                
                top_card = self.deck_pile.top()
                self.deck_pile.pop()
                #calculate distance from card to hand placement
                distance = math.dist((top_card.x,top_card.y),(hand.placement.x,hand.placement.y))
                print(f"Distance: {distance}")
                top_card.delta_x = abs(top_card.x - hand.placement.x)/20
                top_card.delta_y= abs(top_card.y - hand.placement.y)/20
                print(f"Change X: {top_card.delta_x}")
                print(f"Change Y: {top_card.delta_y}")

                while True:
                    top_card.rect = top_card.image_surface.get_rect(center= (top_card.x,top_card.y))
                    self.game.display.blit(top_card.image_surface, top_card.rect)
                    top_card.x-= top_card.delta_x 
                    top_card.y+= top_card.delta_y
                    if top_card.x <= hand.placement.x or top_card.y >= hand.placement.y:
                        break
                
                hand.add_card(top_card)
                #update THIS hand object with a new x and y
                hand.placement.x -= 15 
                hand.placement.y -= 20 #<---- next placement
                

                #try to delay for 1 second
                #TODO make the cards passing slower
                
                    
                    


                
                    
                
        self.printTest()   




    def printTest(self):
            #loop through all the hands to test print
        for i, hand in enumerate(self.turn_list):
            #loop through the cards in THAT specific hand
            print(f"hand {hand.order}", end = " ")
            for j, card in enumerate(hand.card_list):
                print(hand.card_list[j].type,end = " ")

            #if hand has an Ace card, show two different sum values
            if hand.hasAce:
                print(f"Hand Sum: {hand.hand_sum}")
                print(f"Upper Hand Sum: {hand.hand_upper_sum}")
            else:
                print(f"Hand Sum: {hand.hand_sum}")