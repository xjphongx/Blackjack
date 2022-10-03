#from scripts.blackjack import run_game
from scripts.game import Game


#Main function will intialize the game 
def main():    
    game = Game()
    while game.running:
        print(game.current_state)
        game.current_state.display()
        print(f"game file: {game.current_state}")
        if game.playing:
            game.game_loop()
        print(f"after gameloop: {game.current_state}")
    #game.current_state.display()
    #game.game_loop()

if __name__ == '__main__':
    main()