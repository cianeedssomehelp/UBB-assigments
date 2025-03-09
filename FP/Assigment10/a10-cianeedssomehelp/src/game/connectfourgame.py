import random
import math
from src.domain.gameboard import ConnectFourBoard, ConnectFourSymbol

class ConnectFourStrategy:

    def play(self, board: ConnectFourBoard) -> tuple:
        pass

class RandomStrategy(ConnectFourStrategy):
    def play(self, board: ConnectFourBoard):
        if len(board.free_squares) == 0:
            board.connect(ConnectFourSymbol.O, 0)
        move = random.choice(board.free_squares)
        board.connect(ConnectFourSymbol.O, move[0])
        return move

class MediumStrategy(ConnectFourStrategy):
    def play(self, board: ConnectFourBoard):
        computer_symbol = ConnectFourSymbol.O
        opponent_symbol = ConnectFourSymbol.X

        for col in range(board.columns):
            if board.is_valid_move(col):
                for row in range(board.rows - 1, -1, -1):
                    if board.data[row][col] == ' ':
                        board.data[row][col] = computer_symbol.name
                        if board.check_four_connected(row, col):
                            board.data[row][col] = ' '
                            board.connect(computer_symbol, col)
                            return row, col
                        board.data[row][col] = ' '
                        break

        for col in range(board.columns):
            if board.is_valid_move(col):
                for row in range(board.rows - 1, -1, -1):
                    if board.data[row][col] == ' ':
                        board.data[row][col] = opponent_symbol.name
                        if board.check_four_connected(row, col):
                            board.data[row][col] = ' '
                            board.connect(computer_symbol, col)
                            return (row, col)
                        board.data[row][col] = ' '
                        break

        random_strategy = RandomStrategy()
        return random_strategy.play(board)


class GeniusStrategy(ConnectFourStrategy):
    def __init__(self, depth: int = 4):
        self.depth = depth

    def play(self, board: ConnectFourBoard):
        best_score = -math.inf
        best_move = None

        for col in range(board.columns):
            if board.is_valid_move(col):
                for row in range(board.rows - 1, -1, -1):
                    if board.data[row][col] == ' ':
                        board.data[row][col] = ConnectFourSymbol.O.name
                        score = self.minimax(board, self.depth, False)
                        board.data[row][col] = ' '

                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
                        break
        if best_move:
            board.connect(ConnectFourSymbol.O, best_move[1])
        return best_move

    def minimax(self, board: ConnectFourBoard, depth: int, is_maximizing: bool) -> int:
        if depth == 0 or board.is_full():
            return self.evaluate_board(board)

        if is_maximizing:
            max_eval = -math.inf
            for col in range(board.columns):
                if board.is_valid_move(col):
                    for row in range(board.rows - 1, -1, -1):
                        if board.data[row][col] == ' ':
                            board.data[row][col] = ConnectFourSymbol.O.name
                            evaluate = self.minimax(board, depth - 1, False)
                            board.data[row][col] = ' '  # Undo move
                            max_eval = max(max_eval, evaluate)
                            break
            return max_eval
        else:
            min_eval = math.inf
            for col in range(board.columns):
                if board.is_valid_move(col):
                    for row in range(board.rows - 1, -1, -1):
                        if board.data[row][col] == ' ':
                            board.data[row][col] = ConnectFourSymbol.X.name
                            evaluate = self.minimax(board, depth - 1, True)
                            board.data[row][col] = ' '  # Undo move
                            min_eval = min(min_eval, evaluate)
                            break
            return min_eval

    def evaluate_board(self, board: ConnectFourBoard) -> int:
        score = 0

        for row in range(board.rows):
            for col in range(board.columns):
                if board.data[row][col] == ConnectFourSymbol.O.name:
                    score += self.evaluate_position(board, row, col, ConnectFourSymbol.O)
                elif board.data[row][col] == ConnectFourSymbol.X.name:
                    score -= self.evaluate_position(board, row, col, ConnectFourSymbol.X)
        return score

    def evaluate_position(self, board: ConnectFourBoard, row: int, col: int, symbol: ConnectFourSymbol) -> int:
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        score = 0

        for dx, dy in directions:
            count = 1
            open_ends = 0

            r, c = row + dx, col + dy
            while 0 <= r < board.rows and 0 <= c < board.columns:
                if board.data[r][c] == symbol.name:
                    count += 1
                elif board.data[r][c] == ' ':
                    open_ends += 1
                    break
                else:
                    break
                r += dx
                c += dy

            r, c = row - dx, col - dy
            while 0 <= r < board.rows and 0 <= c < board.columns:
                if board.data[r][c] == symbol.name:
                    count += 1
                elif board.data[r][c] == ' ':
                    open_ends += 1
                    break
                else:
                    break
                r -= dx
                c -= dy

            if count >= 4:
                score += 1000
            elif count == 3 and open_ends > 0:
                score += 50
            elif count == 2 and open_ends > 1:
                score += 10

        return score

class ConnectFourGame:
    def __init__(self, strategy: ConnectFourStrategy):
        self.__board = ConnectFourBoard()
        self.__strategy = strategy

    def computer_move(self):
        return self.__strategy.play(self.__board)

    def human_move(self, column: int):
        self.__board.connect(ConnectFourSymbol.X, column)

    @property
    def board(self):
        return self.__board