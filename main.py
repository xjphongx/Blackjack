#from scripts.blackjack import run_game
from scripts.game import Game


#Main function will intialize the game 
def main():    
    game = Game()
    while game.running:
        print(game.state_stack[-1])
        game.game_loop()
   

if __name__ == '__main__':
    main()