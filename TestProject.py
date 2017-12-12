import pygame as py
import sys
from pygame.locals import *

WIDTH = 800
HEIGHT = 600
PIECE_SIZE = 85
WHITE = (255,255,255)
class Main:
    def __init__(self):
        self.selected_item = None
        self.odd_row = ['x','x','-','-','-','x','x']
        self.regular_row = ['-','-','-','-','-','-','-']

        self.coordinates = [['x','x','-','-','-','x','x'],
                            ['x', 'x', '-', '-', '-', 'x', 'x'],
                            ['-', '-', 'O', '-', '-', '-', '-'],
                            ['-', 'O', 'O', 'O', 'O', '-', '-'],
                            ['-', '-', 'O', '-', '-', '-', '-'],
                            ['x', 'x', '-', '-', '-', 'x', 'x'],
                            ['x', 'x', '-', '-', '-', 'x', 'x']]

    def evaluate_click(self, mouse_pos):
        row, col = self.getX(mouse_pos[0]), self.getY(mouse_pos[1])
        print((row, col))
        if self.selected_item:
            move = self.validate_move(self.selected_item, row, col)
            if move[0]:
                self.play(self.selected_item,row,col,move[1])
            elif row == self.selected_item[0] and col == self.selected_item[1]:
                self.selected_item = None
            else:
                print("invalid ")
                self.selected_item = None
        else:
            if self.coordinates[row][col] == 'O':
                self.selected_item = [row, col]

    def validate_move(self, piece_position, row, col):
        piece_row, piece_col = piece_position
        if self.coordinates[row][col] != '-':
            return False, None
        if (abs(piece_row - row) == 2) or ((row - piece_row) == 2):
            if col == piece_col:
                next_row = (row - piece_row) // 2 + piece_row
                return True, [next_row, piece_col]
        if (abs(piece_col - col) == 2) or ((col - piece_col) == 2):
            if row == piece_row:
                next_col = (col - piece_col) // 2 + piece_col
                return True, [piece_row, next_col]
        return False,

    def play(self, piece_position, row, col, jump):
        from_row = piece_position[0]
        from_col = piece_position[1]
        self.coordinates[row][col] = 'O'
        self.coordinates[from_row][from_col] = '-'
        if jump:
            self.coordinates[jump[0]][jump[1]] = '-'
            self.selected_item = [row, col]
            self.selected_item = None


    def draw(self):
        for index, x in enumerate(self.odd_row):
            if x != 'x':
                py.draw.rect(screen,WHITE,(100 + (index * PIECE_SIZE), 0, PIECE_SIZE, PIECE_SIZE),5)
                py.draw.rect(screen, WHITE, (100 + (index * PIECE_SIZE), PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
        for index, x in enumerate(self.regular_row):
            if x != 'x':
                py.draw.rect(screen, WHITE, (100 + (index * PIECE_SIZE), 2 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
                py.draw.rect(screen, WHITE, (100 + (index * PIECE_SIZE), 3 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
                py.draw.rect(screen, WHITE, (100 + (index * PIECE_SIZE), 4 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
        for index, x in enumerate(self.odd_row):
            if x != 'x':
                py.draw.rect(screen, WHITE, (100 + (index * PIECE_SIZE), 5 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
                py.draw.rect(screen, WHITE, (100 + (index * PIECE_SIZE), 6 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
        font = py.font.SysFont('Calibri', 50, False, False)
        for r in range(len(self.coordinates)):
            for c in range(len(self.coordinates[r])):
                mark = self.coordinates[r][c]
                color = (255, 0, 0)
                if mark != '-' and mark != 'x':
                    mark_text = font.render(self.coordinates[r][c], True, color)
                    x = 100 + (r * PIECE_SIZE) + (PIECE_SIZE / 2)
                    y = c * PIECE_SIZE + (PIECE_SIZE / 2)
                    screen.blit(mark_text, [x - mark_text.get_width() / 2, y - mark_text.get_height() / 2])

    def getX(self, pos):
        x = pos
        for i in range(0, 7):
            if x < 100 + (i * PIECE_SIZE):
                return i - 1
        return 6

    def getY(self, pos):
        y = pos
        for i in range(0, 7):
            if y < i * PIECE_SIZE:
                return i - 1
        return 6

py.init()
size = (WIDTH, HEIGHT)
screen = py.display.set_mode(size)
clock = py.time.Clock()
game = Main()
done = False
while not done:
    for event in py.event.get():  # User did something
        if event.type == py.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == py.KEYDOWN:
            entry = str(event.key)
        if event.type == py.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = py.mouse.get_pos()
            game.evaluate_click(py.mouse.get_pos())

    screen.fill((0,   0,   0))

    game.draw()

    py.display.flip()

    clock.tick(60)

py.quit()
