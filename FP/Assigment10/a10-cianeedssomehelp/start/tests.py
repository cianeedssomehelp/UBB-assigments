import unittest
from src.domain.gameboard import ConnectFourBoard, ConnectFourSymbol, InvalidMoveException, GameOverException
from src.game.connectfourgame import ConnectFourGame, RandomStrategy, MediumStrategy, GeniusStrategy


class TestConnectFour(unittest.TestCase):
    def test_board_initialization(self):
        board = ConnectFourBoard()
        self.assertEqual(board.rows, 6)
        self.assertEqual(board.columns, 7)
        self.assertEqual(len(board.free_squares), 42)
        self.assertTrue(all(cell == ' ' for row in board.data for cell in row))

    def test_valid_move(self):
        board = ConnectFourBoard()
        self.assertTrue(board.is_valid_move(0))
        board.connect(ConnectFourSymbol.X, 0)
        self.assertTrue(board.is_valid_move(0))
        self.assertEqual(board.data[5][0], 'X')

    def test_invalid_move_out_of_bounds(self):
        board = ConnectFourBoard()
        with self.assertRaises(InvalidMoveException):
            board.connect(ConnectFourSymbol.X, -1)
        with self.assertRaises(InvalidMoveException):
            board.connect(ConnectFourSymbol.X, 7)



    def test_game_over_vertical_win(self):
        board = ConnectFourBoard()
        try:
            for _ in range(3):
                board.connect(ConnectFourSymbol.X, 0)
                board.connect(ConnectFourSymbol.O, 1)
            board.connect(ConnectFourSymbol.X, 0)  # X wins vertically
        except GameOverException as e:
            self.assertEqual(str(e), "Repository Exception: X wins!")

    def test_human_move(self):
        game = ConnectFourGame(RandomStrategy())
        game.human_move(0)
        self.assertEqual(game.board.data[5][0], 'X')



if __name__ == '__main__':
    unittest.main()
