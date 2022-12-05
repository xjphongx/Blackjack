
import pygame
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
        self.back_button = Button(x=325,y=50,image=back_image,scale=.07)
        self.dealer = Dealer(self.game, self)
        self.deck_pile = DeckPile()
        self.deck_pile.load_cards_to_deck()
        self.deck_pile.shuffle()
        self.discard_pile = DiscardPile()

        #temporary button
        confirm_button_image = pygame.image.load("images/buttons/confirm_button.png").convert_alpha()
        self.confirm_button = Button(x=self.game.display_width/2,y= self.game.display_height/2-140,image=confirm_button_image,scale=.07)
        play_again_image = pygame.image.load("images/buttons/play_again_button.png").convert_alpha()
        self.play_again_button = Button(x=self.game.display_width/2,y= self.game.display_height/2-100,image= play_again_image, scale=.07)
        strategy_card_button_image = pygame.image.load("images/buttons/strategy_card.png").convert_alpha()
        self.strategy_card_button = Button(x=150,y=825,image=strategy_card_button_image,scale = .07)
        self.strategy_card_image = pygame.image.load("images/Simple_Blackjack_Strategy.png").convert_alpha()
        self.card_rect = self.strategy_card_image.get_rect(center=(self.game.display_width/2,self.game.display_height/2))
      
        transparent_image = pygame.image.load("images/transparent_image.png").convert_alpha()
        self.transparent_image_button = Button(x=0,y=0,image=transparent_image,scale= 2)

        self.ring_row = Ring_Row(self.game, self)
        self.bet_menu = Bet_Menu(self.game, self) 
        self.cursor = Cursor(self.game) 
        self.player = Player(self.game, self)
        self.turn_list = [] #empty turn list
        self.gameplay_counter = 0
        self.round_over = False #used to display play again button
    
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
        if self.playing:
            self.start_round()
        else:
            self.game.draw_text("How many hands are you playing?", 
                        50, 
                        self.game.display_width/2,
                        self.game.display_height/5)
        #controls the confirm and play again buttons to switch between the two
        if self.round_over == False:
            self.display_confirm_button()
        else:
            self.display_play_again_button()
        
        #temp button
        if self.back_button.draw(self.game.display):
            #TODO save player funds, and card piles
            self.ring_row.clear() #clears the row 
            self.game.actions["back"] = True

        #render the clickable button
        #Display the transparent image button over the WHOLE gameboard if the button is NOT ACTIVE
        if self.transparent_image_button.isActive == True:
            if self.transparent_image_button.draw(self.game.display):
                    self.strategy_card_button.isActive = False
                    self.transparent_image_button.isActive = False  
            #blit the card image on top of the transparent background
            self.game.display.blit(self.strategy_card_image,self.card_rect)       
        #Display the strategy card button for player access if the button is NOT ACTIVE
        elif self.strategy_card_button.isActive == False: 
            if self.strategy_card_button.draw(self.game.display):
                self.strategy_card_button.isActive = True
                self.transparent_image_button.isActive = True
        
    #state change to the title
    def update(self,actions):
        if actions["back"]:
            self.exit_state()
        self.game.reset_actions()

#Gameboard helper function below
    #This function displays and adds functionality to the confirm button
    def display_confirm_button(self):
        #checks if player is deciding, if clicked, pass out cards
        if self.confirm_button.isActive == False: 
                #if the ring row is not empty and ring row has valid bets, do this
                if not self.ring_row.isEmpty and self.ring_row.isValidBet: 
                    if self.confirm_button.draw(self.game.display): #figure out how to clear this button
                        self.gameplay_counter += 1
                        #combine the player and dealer hands, player goes first
                        self.turn_list.extend(self.dealer.hand_list)
                        self.player.hand_list.reverse() #reserves the player list 
                        self.turn_list.extend(self.player.hand_list)
                        self.turn_list.reverse() #makes sure the player is dealt cards first
                        self.confirm_button.isActive = True #removes the confirm button from screen
                        self.filter_List() #removes the integer values in the turnlist        
                        #set ring bets to hand bets and update current bet to be the round's current bet
                        for i , hand in enumerate(self.turn_list[:-1]):
                            #sets the hand bet amount = ring bet amount
                            hand.bet_amount = self.ring_row.ring_map[hand.order].bet_amount
                            self.player.current_bet += hand.bet_amount #updates the round's current bet
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
        #display button
        if self.play_again_button.draw(self.game.display) == True:
            #Before starting the next round, check then shuffle the discard pile into the deck pile
            if self.deck_pile.size <= 50:
                #combine discard pile into deck pile and reshuffle
                self.deck_pile.combine(self.discard_pile) #takes the stack object as an argument
                self.discard_pile.clear()
                self.deck_pile.shuffle()
            #Move all the cards on the board to the discard pile
            for i, hand in enumerate(self.turn_list):  
                #update funds after round is over 
                self.player.add_funds((hand.bet_amount+hand.win_amount))              
                for j , card in enumerate(hand.card_list):
                    self.discard_pile.push(card)
                #reset all hands objects in memory 
                hand.reset_hand()
            #reset all the objects so the next round can start
            self.player.reset_UI()
            self.delete_extra_hands()
            self.turn_list.clear()     
            self.ring_row.clear()
            self.confirm_button.isActive = False
            self.round_over = False #next round is active
            self.playing = False

    #function filter list uses a simple algorithm to search and replace the list
    def filter_List(self):
        temp_list = []   #temperary list to contain hand objects     
        for i, hand in enumerate(self.turn_list): #cycles and gets the hand 
            if isinstance(hand, Hand): #test if hand is a hand object
                temp_list.append(hand)
        self.turn_list = temp_list.copy() #turn list is replaced with the filtered list
        temp_list.clear()
        
    #function hit allows the player to add one card to the current hand object"
    def hit(self,hand):
        #get the top card
        top_card = self.deck_pile.top()
        self.deck_pile.pop()
        #calculate distance from card to hand placement
        top_card.delta_x = abs(top_card.x - hand.placement.x)/100
        top_card.delta_y = abs(top_card.y - hand.placement.y)/100
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
            hand.placement.x -= 110 #updates to the left
        else:
            hand.placement.x -= 20  #updates the player's hand ontop
            hand.placement.y -= 20 
        
    #function bust will dispute the bets after the round is done
    #player bust and went over 21, 
    #dealer takes the bets but leaves the cards there for reference
    def bust(self, hand):
        hand.bust = True
        hand.isTurn = False
        #if player bust. take the bet at the ring
        if hand.order in self.ring_row.ring_map.keys():
            #this is the ring object based on key(hand's order)
            hand.lost_amount -= hand.bet_amount
            hand.bet_amount = 0 
            self.ring_row.ring_map[hand.order].hasChip = False  #for single hand in ring
            hand.hasChip = False #for hands in split
        #This section is for extra hands when spliting 
        if hand.isExtra:
            hand.hasChip = False
    
    #function compare_hand will compare the dealer's hand to all the player's hand and resolve winning condition
    def compare_hand(self, dealer_hand: Hand):
        for i, player_hand in enumerate(self.turn_list[:-1]):
            #only compare hands when the player hand is NOT busted
            if player_hand.bust == False:
                #Dealer has smaller hand than player's current hand, player wins
                if dealer_hand.hand_sum < player_hand.hand_sum:
                    player_hand.win_amount = player_hand.bet_amount #updates the hand's win notification
                    self.player.win_amount += player_hand.bet_amount*2 #updates the player's Fund notification
                    player_hand.bust = True #prevent constant looping 
                #Dealer and Player both push
                elif dealer_hand.hand_sum == player_hand.hand_sum:
                    #do nothing to the bet and move to the next hand
                    self.player.win_amount += player_hand.bet_amount #updates the player's fund notification
                    player_hand.bust = True #prevent constant looping 
                #Dealer has bigger hand than player's current hand, dealer wins            
                else: 
                    self.bust(player_hand)
        self.round_over = True

    #function player_win gives the all NON-busted hand the winning bets 
    def player_win(self):
        for i, hand in enumerate(self.turn_list[:-1]):
            if hand.bust == False:
                self.player.win_amount += hand.bet_amount*2
                hand.win_amount = hand.bet_amount
                hand.bust = True
        self.round_over = True

    #function pass cards will give out 2 cards to each active hand
    def pass_cards(self):
        #intial passing of cards to each hand and dealer, only passes out 2 cards
        #this algorithm passes out cards in circle order from hand 1 - 5 and dealer's hand
        print(f"Gameplay {self.gameplay_counter}")
        for rotation in range(2):
            for i, hand in enumerate(self.turn_list):
                #edge case where dealer's last card will be faced down
                if rotation == 1 and hand.isDealer:
                    #top_card = self.deck_pile.top()
                    #top_card.isFaceDown = True
                    self.deck_pile.top().isFaceDown = True
                #add the top card into the hand in turn list
                self.hit(hand)
                #TODO make the cards passing slower           
        self.printTest()   

    def printTest(self):
            #loop through all the hands to test print
        for i, hand in enumerate(self.turn_list):
            #loop through the cards in THAT specific hand
            print(f"hand {hand.order}{hand}", end = " ")
            for j, card in enumerate(hand.card_list):
                print(hand.card_list[j].type,end = " ")
            #if hand has an Ace card, show two different sum values
            if hand.hasAce:
                print(f"Hand Sum: {hand.hand_sum}")
                print(f"Upper Hand Sum: {hand.hand_upper_sum}")
            else:
                print(f"Hand Sum: {hand.hand_sum}")

    #This function checks if any of the player's hands busted
    def check_player_hand_list(self)-> bool:
        bust_count = 0 #keeps track of how many hands busted
        for i , hand in enumerate(self.turn_list[:-1]):
            if hand.bust:
                bust_count+=1
        if bust_count == len(self.turn_list[:-1]):
            return True
        return False

    def start_round(self):       
    #TODO THERE IS A BUG WHERE DEALER GETS A BLACKJACK AND THE BOARD IS GONE
    # it goes into the next round, NOT play again button is found 

        #Check case where dealer has a blackjack to immediately end the game and collect bets
        if self.turn_list[-1].hasAce and (self.turn_list[-1].hand_upper_sum == 21):
            #revealed facedown card, dealer's hand sum, and blit the all cards on screen
            self.turn_list[-1].card_list[-1].isFaceDown = False
            self.turn_list[-1].hand_sum = 21
            self.game.draw_text(f"{self.turn_list[-1].hand_sum}",30,self.turn_list[-1].x, self.turn_list[-1].y-100)
            #cycle through the turn list and bust every hand except dealers
            for j, hand in enumerate(self.turn_list):
                hand.display(self.game.display)
                if not hand.isDealer and not (hand.hand_sum == 21 or hand.hand_upper_sum == 21):
                    self.bust(hand) #bust every hand except for hand with 21      
            self.round_over = True #ends the round
        #continue with game when dealer DOES NOT have an immediate blackjack
        else: #display the cards from each hand
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
                    #Case where player is dealt a Blackjack with the first two cards, hand MUST stand
                    elif hand.hasAce and hand.hand_upper_sum == 21 and len(hand.card_list) == 2 and hand.isTurn:
                        hand.stand = True
                        hand.hand_sum = hand.hand_upper_sum
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90)               
                    #has ace and equals to 21
                    elif hand.hasAce and hand.hand_upper_sum == 21:
                        if hand.stand:
                            hand.hand_sum = 21
                            self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y+90) 
                        else:
                            self.game.draw_text(f"{hand.hand_sum} or {hand.hand_upper_sum}",30,hand.x, hand.y+90)
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
                    
                #DEALER LOGIC and Winning condition logic,
                #continue to hit until 17 -21 or bust
                if hand.isDealer and hand.isTurn:
                    #reveal the face down card and sum
                    hand.card_list[-1].isFaceDown = False
                    #Case where dealer has a an ACE and resulted in a blackjack
                    if hand.hasAce and hand.hand_upper_sum == 21:
                        hand.hand_sum = 21
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y-100)  
                    #Case where all hands bust, dealer wins and does not hit hand
                    elif self.check_player_hand_list(): #True if atlease 1 hand bust 
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y-100)
                        self.round_over = True  #end the round 
                    #dealer has an ace card hits until 17 or more
                    elif hand.hasAce and hand.hand_upper_sum < 17:
                        self.hit(hand)
                        self.game.draw_text(f"{hand.hand_sum} or {hand.hand_upper_sum}",30,hand.x, hand.y-100)     
                    #dealer has an ace and hits until the range 17 - 21
                    elif hand.hasAce and (hand.hand_upper_sum >=17 and hand.hand_upper_sum <21):
                        hand.hand_sum = hand.hand_upper_sum
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y-100)  
                        self.compare_hand(hand)    
                    #dealer has less than 17 and hits hand
                    elif hand.hand_sum < 17:
                        self.hit(hand)
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y-100) 
                    #dealer has hand between 17 and 21 
                    elif hand.hand_sum >= 17 and hand.hand_sum <= 21:
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y-100)
                        self.compare_hand(hand) 
                    #dealer BUSTs, so give all non busted hands 2x their current hand
                    else:
                        self.bust(hand)
                        self.game.draw_text(f"{hand.hand_sum}",30,hand.x, hand.y-100)
                        self.player_win() #pass out winnings 
                #update the player's winning notification
                if self.round_over:
                    #update the player's difference
                    self.player.round_difference_amount = self.player.win_amount - self.player.current_bet
    
    #This function will go through the turn list and delete the memory address of any extra hand
    def delete_extra_hands(self):
        print(f"before delete hands {self.turn_list}")
        for i, hand in enumerate(self.turn_list):
            if hand.isExtra:
                del self.turn_list[i]
        print(f"after delete hands {self.turn_list}")
                
                        
                        
                        