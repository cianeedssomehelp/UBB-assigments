import string

from src.game.connectfourgame import ConnectFourGame
from src.domain.gameboard import ConnectFourBoard, InvalidMoveException, GameOverException


class ConnectFourUi:
    def __init__(self, strategy):
        self.__strategy = strategy
        self.__game = ConnectFourGame(self.__strategy)

    def start(self):
        print("Welcome to Connect Four!")
        print("Rules: ")
        print("1) In this game, your aim is to connect four of your simbols, before your opponent does.")
        print("2) One of your symbols is dropped on a free square of the column of your choosing.")
        print("3) Four can be connected horizontally, vertically or even diagonally.")
        print("And lastly, have fun!")
        print("Here's the game board: ")
        print(ConnectFourBoard())

        human_turn = True
        while True:
            try:
                if human_turn:
                    move = input("Enter your move (e. g. A): ")
                    column = ord(move[0].upper()) - ord('A')
                    self.__game.human_move(column)
                else:
                    move = self.__game.computer_move()
                    move_letter = string.ascii_uppercase[move[0]]
                    print(f"Computer moved at column {move_letter}.")
                    print(self.__game.board)
                human_turn = not human_turn
                if self.__game.board.is_full():
                    print("Looks like it's a draw, there are no more moves left.")
                    break
            except ValueError as e:
                print(e)
                human_turn = True
            except InvalidMoveException as ie:
                print(ie)
                human_turn = True
            except GameOverException as goe:
                if human_turn:
                    print("Good job, you won!")
                else:
                    print("You've just lost the game, better luck next time! :(")
                print(self.__game.board)
                break