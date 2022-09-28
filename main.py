#from scripts.blackjack import run_game
from scripts.game import Game


#Main function will intialize the game 
def main():    
    game = Game()
    while game.running:
        game.current_state.display_menu()
        game.game_loop()

if __name__ == '__main__':
    main()