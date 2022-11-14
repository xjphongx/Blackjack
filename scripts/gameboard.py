
import pygame, math
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
        self.min_bet = 50
        back_image = pygame.image.load("images/buttons/back_button.png").convert_alpha()
        self.back_button = Button(325, 50, back_image, self.game.IMAGE_SCALE)
        self.dealer = Dealer(self.game, self)
        self.deck_pile = DeckPile()
        self.deck_pile.load_cards_to_deck()
        self.discard_pile = DiscardPile()
        for i in range(8):     #shuffle the deck when starting the gameboard
            self.deck_pile.cut_deck()
            self.deck_pile.casino_shuffle()          
        #temporary button
        confirm_button_image = pygame.image.load("images/buttons/confirm_button.png").convert_alpha()
        self.confirm_button = Button(self.game.display_width/2, self.game.display_height/2, confirm_button_image,scale=.1)
        play_again_image = pygame.image.load("images/buttons/play_again_button.png").convert_alpha()
        self.play_again_button = Button(1000,100 , play_again_image, scale=.1)

        self.ring_row = Ring_Row(self.game, self)
        self.bet_menu = Bet_Menu(self.game, self) 
        self.cursor = Cursor(self.game) 
        self.player = Player(self.game, self)
        self.turn_list = [] #empty turn list
    
    #This function adds functionality to the gameboard state
    def render(self,display):
        display.fill(self.game.background_color)
        #set up dealer
        self.game.draw_text("Dealer", 30, self.game.display_width/2,125)
        self.game.display.blit(self.dealer.dealer_image_surface, self.dealer.rect)           
        #set up deck
        self.game.display.blit(self.deck_pile.image_surface, self.deck_pile.rect) 
        self.game.draw_text(f"{self.deck_pile.size}", 30, self.deck_pile.rect.centerx, self.deck_pile.rect.centery+100)
        #set up discard pile
        self.game.display.blit(self.discard_pile.image_surface, self.discard_pile.rect)
        self.game.draw_text(f"{self.discard_pile.size}", 30, self.discard_pile.rect.centerx, self.discard_pile.rect.centery+100)       
        #betting bar and functionality
        self.bet_menu.display()
        #hand ring functionality
        self.ring_row.display()
        #start game
        self.check_playing()
        self.display_confirm_button()
        self.display_play_again_button()
        
        #render the clickable button
        if self.back_button.draw(self.game.display):
            self.ring_row.clear() #clears the row 
            self.game.actions["back"] = True

    #state change to the title
    def update(self,actions):
        if actions["back"]:
            self.exit_state()
        self.game.reset_actions()

#Gameboard helper function below

    #This function checks if the game is playing
    def check_playing(self):
        if self.playing:
            #Start the game
            self.start_game()
        else:
            self.game.draw_text("How many hands are you playing?", 
                        50, 
                        self.game.display_width/2,
                        self.game.display_height/5)

    #This function displays and adds functionality to the confirm button
    def display_confirm_button(self):
        #checks if player is deciding, if clicked, pass out cards
        if self.confirm_button.isActive == False: 
                #if the ring row is not empty and ring row has valid bets, do this
                if not self.ring_row.isEmpty and self.ring_row.isValidBet: 
                    if self.confirm_button.draw(self.game.display): #figure out how to clear this button
                        #combine the player and dealer hands, player goes first
                        self.turn_list.extend(self.dealer.hand_list)
                        self.turn_list.extend(self.player.hand_list)
                        self.turn_list.reverse() #makes sure the player is dealt cards first
                        self.confirm_button.isActive = True #removes the confirm button from screen
                        self.filter_List()
                        #set ring bets to hand bets
                        for i , hand in enumerate(self.turn_list[:-1]):
                            #sets the hand bet amount = ring bet amount
                            hand.bet_amount = self.ring_row.ring_map[hand.order].bet_amount
                            self.ring_row.ring_map[hand.order].bet_amount = 0 #sets the ring bet amount = 0 to reset the ring
                        #pass out cards
                        self.pass_cards()
                        #set first hand's turn and start game
                        self.turn_list[0].isTurn = True
                        self.playing = True
                else:
                     #if player clicks the confirm button and the row is empty and not valid, do nothing
                     self.confirm_button.draw(self.game.display) #continue to display
    
    def display_play_again_button(self):
        if self.play_again_button.draw(self.game.display):
            print("hi")

    #function filter list uses a simple algorithm to search and replace the list
    def filter_List(self):
        temp_list = []   #temperary list to contain hand objects     
        for i, hand in enumerate(self.turn_list): #cycles and gets the hand 
            if isinstance(hand, Hand): #test if hand is a hand object
                temp_list.append(hand)
        self.turn_list = temp_list.copy() #turn list is replaced with the filtered lsit
        temp_list.clear()
        
    #function hit allows the player to add one card to the current hand object"
    def hit(self,hand):
        #get the top card
        top_card = self.deck_pile.top()
        self.deck_pile.pop()
        #calculate distance from card to hand placement
        #distance = math.dist((top_card.x,top_card.y),(hand.placement.x,hand.placement.y))
        #print(f"Distance: {distance}")
        top_card.delta_x = abs(top_card.x - hand.placement.x)/60
        top_card.delta_y = abs(top_card.y - hand.placement.y)/60
        #print(f"Change X: {top_card.delta_x}")
        #print(f"Change Y: {top_card.delta_y}")
        #Loop card blit animation from deck pile to targeted placement
        while True:
            top_card.rect = top_card.card_back_surface.get_rect(center= (top_card.x,top_card.y))
            self.game.display.blit(top_card.card_back_surface, top_card.rect)
            top_card.x-= top_card.delta_x 
            top_card.y+= top_card.delta_y
            if top_card.x <= hand.placement.x or top_card.y >= hand.placement.y:
                break
        #add top card to current hand object
        hand.add_card(top_card)
        #check if the hand is dealer or player for specified placement
        if hand.isDealer:
            hand.placement.x -= 125 #updates to the left
        else:
            hand.placement.x -= 20  #updates the player's hand ontop
            hand.placement.y -= 20 
        
    #function bust will dispute the bets after the round is done
    def bust(self, hand):
        hand.bust = True
        hand.isTurn = False
        #player bust and went over 21, 
        #dealer takes the bets but leaves the cards there for reference
        #if player bust. take the bet at the ring
        if hand.order in self.ring_row.ring_map.keys():
             #this is the ring object based on key(hand's order)
            hand.bet_amount = 0 
            self.ring_row.ring_map[hand.order].hasChip = False #TODO add notification that bet was lost
        
    
    
    #function compare_hand will compare the dealer's hand to all the player's hand and resolve winning condition
    def compare_hand(self, dealer_hand: Hand):
        for i, player_hand in enumerate(self.turn_list[:-1]):
            #only compare hands when the player hand is NOT busted
            if player_hand.bust == False:
                #dealer has smaller hand than player's current hand, player wins
                if dealer_hand.hand_sum < player_hand.hand_sum:
                    player_hand.bet_amount += player_hand.bet_amount
                    player_hand.bust = True #prevent constant looping 
                #dealer has bigger hand than player's current hand, dealer wins
                else: 
                    
                    #player_hand.bet_amount = 0
                    self.bust(player_hand)

    #function player_win gives the all NON-busted hand the winning bets 
    def player_win(self):
        for i, hand in enumerate(self.turn_list[:-1]):
            if hand.bust == False:
                #TODO add winning notification
                hand.bet_amount += hand.bet_amount
                hand.bust = True

    #function pass cards will give out 2 cards to each active hand
    def pass_cards(self):
        print(self.turn_list)
        #intial passing of cards to each hand and dealer, only passes out 2 cards
        #this algorithm passes out cards in circle order from hand 1 - 5 and dealer's hand
        for rotation in range(2):
            for i, hand in enumerate(self.turn_list):
                #edge case where dealer's last card will be faced down
                if rotation == 1 and hand.isDealer:
                    top_card = self.deck_pile.top()
                    top_card.isFaceDown = True
                #add the top card into the hand in turn list
                self.hit(hand)
 
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

    def start_game(self):       
        #Check case where dealer has a blackjack to immediately end the game and collect bets
        if self.turn_list[-1].hasAce and (self.turn_list[-1].hand_upper_sum == 21):
            print("has Blackjack and everyone bust")
            self.turn_list[-1].card_list[-1].isFaceDown = False
            #cycle through the turn list until the dealer's index to bust every hand
            for i, hand in enumerate(self.turn_list[:-1]):
                self.bust(hand) #bust every hand
                
        else: #continue with game when dealer DOES NOT have blackjack
            #display the cards from each hand
            #and display the menu to choose from
            for i, hand in enumerate(self.turn_list):
                #display the hand
                hand.display(self.game.display)
                
                #PLAYER LOGIC
                if not hand.isDealer:
                    #display all hand's sum value on the board
                    if hand.hasAce and hand.hand_upper_sum < 21:
                        if hand.stand:
                            hand.hand_sum = hand.hand_upper_sum
                            self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)   
                        else:
                            self.game.draw_text(f"{hand.hand_sum} or {hand.hand_upper_sum}",30,hand.x, hand.y+90)   
                    #has ace and equals to 21
                    elif hand.hasAce and hand.hand_upper_sum == 21:
                        hand.hand_sum = 21
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90) 
                    #has ace and is above 21, display the lower sum
                    elif hand.hasAce and hand.hand_upper_sum >21:
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)
                    #display hand sum no matter what
                    else:
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)
                    #check if hand is busted
                    if hand.hand_sum > 21:
                        self.bust(hand)
                        self.turn_list[i+1].isTurn = True #sets the next turn 
                    #check if player stands on hand
                    if hand.stand == True:
                        hand.isTurn = False
                        self.turn_list[i+1].isTurn = True
                    #display action menu if its the current hand's turn
                    if hand.isTurn: #this has to be placed at the end to prevent a display bug
                        hand.action_menu.display() #this is where player clicks action buttons
                    
                #DEALER LOGIC, continue to hit until 17 -21 or bust
                if hand.isDealer and hand.isTurn:
                    #reveal the face down card and sum
                    hand.card_list[-1].isFaceDown = False
                    #dealer has a an ACE and resulted in a blackjack
                    if hand.hasAce and hand.hand_upper_sum == 21:
                        hand.hand_sum = 21
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)    
                    #dealer has an ace card hits until 17 or more
                    elif hand.hasAce and hand.hand_upper_sum < 17:
                        self.hit(hand)
                        self.game.draw_text(f"{hand.hand_sum} or {hand.hand_upper_sum}",30,hand.x, hand.y+90)     
                    #dealer has an ace and hits until the range 17 - 21
                    elif hand.hasAce and (hand.hand_upper_sum >=17 and hand.hand_upper_sum <21):
                        hand.hand_sum = hand.hand_upper_sum
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)     
                    #dealer has less than 17 and hits hand
                    elif hand.hand_sum < 17:
                        self.hit(hand)
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)
                    #dealer has blackjack
                    elif hand.hand_sum == 21:
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)
                        self.compare_hand(hand)          
                    #dealer has hand between 17 and 21 WITHOUT ace card 
                    elif hand.hand_sum >= 17 and hand.hand_sum < 21:
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)
                        self.compare_hand(hand) 
                    #dealer BUSTs, so give all non busted hands 2x their current hand
                    else:
                        self.game.draw_text("Busted",60, hand.x, hand.y+110)
                        self.bust(hand)
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)
                        self.player_win() #pass out winnings 
                        
                        
                        