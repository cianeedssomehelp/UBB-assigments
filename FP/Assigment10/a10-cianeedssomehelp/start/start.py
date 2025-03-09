from src.ui.ui import *
from src.gui.gui import *
from src.game.connectfourgame import RandomStrategy, MediumStrategy, GeniusStrategy

def main():
    while True:
        choice = input("Would you like to run the game text-based or in the console (type a or b)? ").strip().lower()
        if choice == "a":
            while True:
                try:
                    difficulty = input(
                        "Which difficulty would you like to play (e.g. easy, medium, hard)? ").strip().lower()
                    if difficulty == 'easy':
                        strategy = RandomStrategy()
                    elif difficulty == 'medium':
                        strategy = MediumStrategy()
                    elif difficulty == 'hard':
                        strategy = GeniusStrategy()
                    else:
                        raise ValueError("Invalid difficulty. Please choose 'easy', 'medium', or 'hard'.")

                    ui = ConnectFourUi(strategy)
                    ui.start()
                    break
                except ValueError as ve:
                    print(ve)
            break
        elif choice == "b":
            while True:
                try:
                    difficulty = input("Which difficulty would you like to play (e.g. easy, medium, hard)? ").strip().lower()
                    if difficulty == 'easy':
                        strategy = RandomStrategy()
                    elif difficulty == 'medium':
                        strategy = MediumStrategy()
                    elif difficulty == 'hard':
                        strategy = GeniusStrategy()
                    else:
                        raise ValueError("Invalid difficulty. Please choose 'easy', 'medium', or 'hard'.")

                    gui = ConnectFourGui(strategy)
                    gui.play_game()
                    break
                except ValueError as ve:
                    print(ve)
            break
        else:
            print("Invalid choice. Please type 'a' for text-based or 'b' for console.")

if __name__ == "__main__":
    main()
