import pygame as py
import sys
from Object import Object
from pygame.locals import *


class Game:
    def __init__(self, width, height, name="Project 2 Game"):
        py.init()
        self.clock = py.time.Clock()
        self.screen = py.display.set_mode((width, height))
        py.display.set_caption(name)
        self.all_sprites = py.sprite.Group()
        self.player = Object("Resources/MM.png", 0, 0)
        self.player2 = Object("Resources/MM.png", 300, 300)
        # self.circle = obj.Object("Resources/circle.png", 300, 300, self.all_sprites)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        self.clicked = False
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def update(self, tick_rate):
        # Events
        self.clock.tick(tick_rate)
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for sprite in self.all_sprites:
                        sprite.drag(event)
            elif event.type == MOUSEBUTTONUP:
                for sprite in self.all_sprites:
                    if event.button == 1:
                        sprite.dragging = False
            elif event.type == MOUSEMOTION:
                for sprite in self.all_sprites:
                    sprite.drag(event)
        # Update
        self.all_sprites.update()

    def draw(self):
        # Draw
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        py.display.flip()
