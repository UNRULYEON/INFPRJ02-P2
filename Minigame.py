import pygame as py
import TestProject as tr
from pygame.locals import *
WIDTH = 800
HEIGHT = 600
PIECE_SIZE = 63
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LEVEL = 0

py.init()
size = (WIDTH, HEIGHT)
screen = py.display.set_mode(size)
clock = py.time.Clock()
game = tr.Main(LEVEL)
py.mixer.music.load("Resources/Audio/bgm.wav")
py.mixer.music.set_volume(0.1)
done = False
py.mixer.music.play(loops=-1)
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
        if event.type == py.KEYDOWN:
            if event.key == K_q:
                game = tr.Main(0)
        if event.type == py.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = py.mouse.get_pos()
    if game.levelComplete:
        LEVEL = LEVEL + 1
        game = tr.Main(LEVEL)
    game.update(event)
    screen.fill((0, 0, 0))
    game.draw(screen)
    py.display.flip()
    clock.tick(60)

py.quit()