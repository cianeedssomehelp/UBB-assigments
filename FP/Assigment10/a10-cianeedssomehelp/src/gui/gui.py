import pygame
from src.game.connectfourgame import ConnectFourGame
from src.domain.gameboard import InvalidMoveException, GameOverException

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS = SQUARE_SIZE // 2 - 5
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
SCREEN_SIZE = (WIDTH, HEIGHT)


class ConnectFourGui:
    def __init__(self, strategy):
        self.__strategy = strategy
        self.__game = ConnectFourGame(self.__strategy)
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Connect Four")
        self.font = pygame.font.SysFont("monospace", 75)
        pygame.init()
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        self.SQUARE_SIZE = 100
        self.RADIUS = int(self.SQUARE_SIZE / 2 - 5)
        self.WIDTH = self.COLUMN_COUNT * self.SQUARE_SIZE
        self.HEIGHT = (self.ROW_COUNT + 1) * self.SQUARE_SIZE
        self.size = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.PINK = (255, 0, 255)
        self.PURPLE = (255, 0, 0)
        self.LIGHTBLUE = (0, 255, 255)

    def draw_board(self):
        for r in range(self.ROW_COUNT):
            for c in range(self.COLUMN_COUNT):
                pygame.draw.rect(
                    self.screen, self.LIGHTBLUE,
                    (c * self.SQUARE_SIZE, (self.ROW_COUNT - r) * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE)
                )
                pygame.draw.circle(
                    self.screen, self.BLACK,
                    (c * self.SQUARE_SIZE + self.SQUARE_SIZE // 2,
                     (self.ROW_COUNT - r) * self.SQUARE_SIZE + self.SQUARE_SIZE // 2),
                    self.RADIUS
                )

        for r in range(self.ROW_COUNT):
            for c in range(self.COLUMN_COUNT):
                if self.__game.board.data[r][c] == "X":
                    pygame.draw.circle(
                        self.screen, self.RED,
                        (c * self.SQUARE_SIZE + self.SQUARE_SIZE // 2,
                         (self.ROW_COUNT - r) * self.SQUARE_SIZE + self.SQUARE_SIZE // 2),
                        self.RADIUS
                    )
                elif self.__game.board.data[r][c] == "O":
                    pygame.draw.circle(
                        self.screen, self.YELLOW,
                        (c * self.SQUARE_SIZE + self.SQUARE_SIZE // 2,
                         (self.ROW_COUNT - r) * self.SQUARE_SIZE + self.SQUARE_SIZE // 2),
                        self.RADIUS
                    )
        pygame.display.update()



    def play_game(self):
        running = True
        human_turn = True
        self.draw_board()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, self.BLACK, (0, 0, self.WIDTH, self.SQUARE_SIZE))
                    posx = event.pos[0]
                    if human_turn:
                        pygame.draw.circle(self.screen, self.RED, (posx, self.SQUARE_SIZE // 2), self.RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, self.BLACK, (0, 0, self.WIDTH, self.SQUARE_SIZE))

                    if human_turn:
                        posx = event.pos[0]
                        column = posx // self.SQUARE_SIZE
                        try:
                            self.__game.human_move(column)
                            if self.__game.board.is_full():
                                print("It's a draw!")
                                running = False
                            self.draw_board()
                            human_turn = False
                        except InvalidMoveException as e:
                            print(e)
                        except GameOverException:
                            print("You win!")
                            running = False

                    if not human_turn:
                        try:
                            move = self.__game.computer_move()
                            self.draw_board()
                            human_turn = True
                        except GameOverException:
                            print("Computer wins!")
                            running = False

        pygame.quit()
