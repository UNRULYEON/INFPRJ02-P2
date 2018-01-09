import pygame as py
import sys
from pygame.locals import *
from minigames.vlad.Ball import Ball

WIDTH = 800
HEIGHT = 600
PIECE_SIZE = 63
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

levelComplete = False
class Main:

    def __init__(self, num):
        self.selected_item = None
        self.currentLevel = num
        self.odd_row = ['x', 'x', '-', '-', '-', 'x', 'x']
        self.regular_row = ['-', '-', '-', '-', '-', '-', '-']
        self.levels = [[
['x', 'x', '-', '-', '-', 'x', 'x'],
['x', 'x', '-', '-', '-', 'x', 'x'],
['-', '-', 'O', '-', '-', '-', '-'],
['-', 'O', 'O', 'O', 'O', '-', '-'],
['-', '-', 'O', '-', '-', '-', '-'],
['x', 'x', '-', '-', '-', 'x', 'x'],
['x', 'x', '-', '-', '-', 'x', 'x']],

[['x', 'x', '-', '-', '-', 'x', 'x'],
['x', 'x', '-', 'O', '-', 'x', 'x'],
['-', '-', '-', 'O', '-', '-', '-'],
['-', 'O', 'O', 'O', 'O', 'O', '-'],
['-', '-', '-', 'O', '-', '-', '-'],
['x', 'x', '-', 'O', '-', 'x', 'x'],
['x', 'x', '-', '-', '-', 'x', 'x']],

[['x', 'x', '-', '-', 'O', 'x', 'x'],
['x', 'x', '-', 'O', 'O', 'x', 'x'],
['-', '-', 'O', 'O', 'O', '-', '-'],
['-', 'O', 'O', 'O', 'O', '-', '-'],
['-', '-', 'O', 'O', 'O', '-', '-'],
['x', 'x', '-', 'O', 'O', 'x', 'x'],
['x', 'x', '-', '-', 'O', 'x', 'x']],

[['x', 'x', '-', '-', '-', 'x', 'x'],
['x', 'x', '-', '-', '-', 'x', 'x'],
['-', '-', '-', 'O', 'O', 'O', 'O'],
['-', '-', '-', '-', 'O', 'O', 'O'],
['-', '-', '-', 'O', 'O', 'O', 'O'],
['x', 'x', '-', '-', '-', 'x', 'x'],
['x', 'x', '-', '-', '-', 'x', 'x']],

[['x', 'x', '-', 'O', '-', 'x', 'x'],
['x', 'x', 'O', 'O', 'O', 'x', 'x'],
['-', 'O', 'O', 'O', 'O', 'O', '-'],
['O', 'O', 'O', '-', 'O', 'O', 'O'],
['-', 'O', 'O', 'O', 'O', 'O', '-'],
['x', 'x', 'O', 'O', 'O', 'x', 'x'],
['x', 'x', '-', 'O', '-', 'x', 'x']],
]
        self.coordinates = self.levels[num -1]
        self.balls = py.sprite.Group()
        self.gen()
        self.move_count = 0
        self.win = py.mixer.Sound("minigames/vlad/Resources/Audio/winsound.wav")
        self.reset = py.mixer.Sound("minigames/vlad/Resources/Audio/reset.wav")
        self.post = py.mixer.Sound("minigames/vlad/Resources/Audio/post.ogg")


    def click(self, evt, ball):
        mouse_x, mouse_y = py.mouse.get_pos()
        if evt.type == MOUSEBUTTONDOWN:
            row, col = self.getX(mouse_x), self.getY(mouse_y)
            self.selected_item = [row, col]
            if self.point_collision(evt.pos, ball.rect, ball.mask):
                ball.dragging = True
                mx, my = evt.pos
                ball.offset_x = ball.rect.x - mx
                ball.offset_y = ball.rect.y - my
        elif evt.type == MOUSEBUTTONUP:
            row, col = self.getX(mouse_x), self.getY(mouse_y)
            if self.selected_item:
                move = self.validate_move(self.selected_item, row, col)
                if move[0]:
                    self.play(self.selected_item, row, col, move[1])
                elif row == self.selected_item[0] and col == self.selected_item[1]:
                    self.selected_item = None
                else:
                    #print("invalid ")
                    self.selected_item = None
            ball.dragging = False
        elif evt.type == MOUSEMOTION:
            if ball.dragging:
                mx, my = evt.pos
                ball.rect.x = mx + ball.offset_x
                ball.rect.y = my + ball.offset_y

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
        for sprite in self.balls:
            if sprite.grid == [from_row, from_col]:
                sprite.grid = [row, col]
            if sprite.grid == [jump[0], jump[1]]:
                self.move_count = self.move_count + 1
                sprite.kill()
        if jump:
            self.coordinates[jump[0]][jump[1]] = '-'
            self.selected_item = [row, col]
            self.selected_item = None
            self.reset.play(loops=0)

    def update(self, event):
    	global levelComplete
    	if len(self.balls) == 1:
            levelComplete = True
    	for sprite in self.balls:
    		self.click(event, sprite)
    	self.balls.update()


    def draw(self, screen):
        bg = py.image.load("minigames/vlad/Resources/bg.png").convert_alpha()
        screen.blit(bg, (0, 0))
        ''' ONSCREEN MOVE COUNT
        color = (255, 0, 0)
        font = py.font.SysFont("comicsansms", 40)
        mark_text = font.render('move count:' + str(self.move_count), True, color)
        screen.blit(mark_text, (10, 50))
        '''

        for index, x in enumerate(self.odd_row):
            if x != 'x':
                py.draw.rect(screen, BLACK, (162 + (index * PIECE_SIZE), 30, PIECE_SIZE, PIECE_SIZE), 5)
                py.draw.rect(screen, BLACK, (162 + (index * PIECE_SIZE), 30 + PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
        for index, x in enumerate(self.regular_row):
            if x != 'x':
                py.draw.rect(screen, BLACK, (162 + (index * PIECE_SIZE), 30 + 2 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
                py.draw.rect(screen, BLACK, (162 + (index * PIECE_SIZE), 30 + 3 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
                py.draw.rect(screen, BLACK, (162 + (index * PIECE_SIZE), 30 + 4 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
        for index, x in enumerate(self.odd_row):
            if x != 'x':
                py.draw.rect(screen, BLACK, (162 + (index * PIECE_SIZE),30 + 5 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
                py.draw.rect(screen, BLACK, (162 + (index * PIECE_SIZE),30 + 6 * PIECE_SIZE, PIECE_SIZE, PIECE_SIZE), 5)
        self.balls.draw(screen)

    def point_collision(self, point, rect, mask):
        x, y = point
        x -= rect.x
        y -= rect.y
        try:
            return mask.get_at((x, y))
        except IndexError:
            return False

    def gen(self):
        for r in range(len(self.coordinates)):
            for c in range(len(self.coordinates[r])):
                mark = self.coordinates[r][c]
                if mark != '-' and mark != 'x':
                    x = 162 + (r * PIECE_SIZE) + (PIECE_SIZE / 2)
                    y = 30 + c * PIECE_SIZE + (PIECE_SIZE / 2)
                    Ball("minigames/vlad/Resources/StickyNoteO.png", x - PIECE_SIZE / 2, y - PIECE_SIZE / 2, self.balls,
                         [self.getX(x), self.getY(y)])

    def getX(self, pos):
        x = pos
        for i in range(0, 7):
            if x < 162 + (i * PIECE_SIZE):
                return i - 1
        return 6

    def getY(self, pos):
        y = pos
        for i in range(0, 7):
            if y < 30 + i * PIECE_SIZE:
                return i - 1
        return 6

class RunMinigame():
    def main(lvl):
        global levelComplete
        py.init()
        clock = py.time.Clock()
        screen = py.display.get_surface()
        game = Main(lvl)
        py.mixer.music.load("minigames/vlad/Resources/Audio/bgm.wav")
        py.mixer.music.set_volume(0.1)
        done = False
        py.mixer.music.play(loops=-1)
        while not done:
            for event in py.event.get():
                if event.type == py.QUIT:
                    done = True
                if event.type == py.KEYDOWN:
                    if event.key == K_q:
                        game = Main(lvl)
                if event.type == py.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = py.mouse.get_pos()
                game.update(event)
                screen.fill((0, 0, 0))
                game.draw(screen)
                py.display.flip()
                clock.tick(60)
            if levelComplete is True:
                print("Player completed the level")
                levelComplete = False
                return True
        py.key.set_repeat(1, 20)
        py.quit()

