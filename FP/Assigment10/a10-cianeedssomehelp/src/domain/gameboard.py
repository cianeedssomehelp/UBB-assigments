import string
from enum import Enum

from texttable import Texttable

class InvalidMoveException(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "Repository Exception: " + self.__msg

class GameOverException(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "Repository Exception: " + self.__msg


class ConnectFourSymbol(Enum):
    X = 0
    O = 1

class ConnectFourBoard:
    def __init__(self, rows: int = 6, columns: int = 7):
        self.__rows = rows
        self.__columns = columns
        self.__data = [[' ' for _ in range(columns)] for _ in range(rows)]

        self.__free_squares = []
        for i in range(rows):
            for j in range(columns):
                self.__free_squares.append((i, j))

    def connect(self, symbol: ConnectFourSymbol, column: int):
        if not (0 <= column < self.__columns):
            raise InvalidMoveException(f"Move played outside the board {column}")

        for row in range(self.__rows - 1, -1, -1):
            if self.__data[row][column] == ' ':
                self.__data[row][column] = symbol.name
                self.free_squares.remove((row, column))
                if self.check_four_connected(row, column):
                    raise GameOverException(f"{symbol.name} wins!")
                return
        raise InvalidMoveException(f"Column {column} is full.")

    def check_four_connected(self, row, column) -> bool:
        symbol = self.__data[row][column]
        if symbol == ' ':
            return False

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            r, c = row + dx, column + dy
            while 0 <= r < self.__rows and 0 <= c < self.__columns and self.__data[r][c] == symbol:
                count += 1
                r += dx
                c += dy
            r, c = row - dx, column - dy
            while 0 <= r < self.__rows and 0 <= c < self.__columns and self.__data[r][c] == symbol:
                count += 1
                r -= dx
                c -= dy
            if count >= 4:
                return True
        return False

    def consecutive(self, dx, dy, row, column, symbol):
        count = 0
        r = row + dx
        c = column + dy
        while 0 <= r < self.__rows and 0 <= c < self.__columns and self.__data[r][c] == symbol:
            count += 1
            r += dx
            c += dy
        return count


    @property
    def free_squares(self):
        return self.__free_squares

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    @property
    def data(self):
        return self.__data

    def __str__(self):
        t = Texttable()
        t.header(list(string.ascii_uppercase[:self.__columns]))
        for i in range(0, self.__rows):
            t.add_row(self.__data[i])
        t.add_row(list(string.ascii_uppercase[:self.__columns]))
        return t.draw()

    def is_full(self) -> bool:
        return len(self.__free_squares) == 0

    def is_valid_move(self, column):
        if 0 <= column < self.__columns and self.__data[0][column] == ' ':
            return True
        return False

if __name__ == "__main__":
    cb = ConnectFourBoard(6, 7)
    try:
        cb.connect(ConnectFourSymbol.X, 0)
        cb.connect(ConnectFourSymbol.O, 1)
        cb.connect(ConnectFourSymbol.X, 0)
        cb.connect(ConnectFourSymbol.O, 1)
        cb.connect(ConnectFourSymbol.X, 0)
        cb.connect(ConnectFourSymbol.O, 1)
        cb.connect(ConnectFourSymbol.X, 0)  # X wins vertically
    except GameOverException as e:
        print(e)
    print(cb)
