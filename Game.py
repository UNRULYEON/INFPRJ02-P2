import pygame as py
import sys
import Object as obj
import DragObject as drag
from pygame.locals import *


class Game:
    def __init__(self, width, height, name="Project 2 Game"):
        py.init()
        self.clock = py.time.Clock()
        self.screen = py.display.set_mode((width, height))
        py.display.set_caption(name)
        self.all_sprites = py.sprite.Group()
        self.player = obj.Object("Resources/MM.png", 0, 0)
        self.all_sprites.add(self.player)
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
            drag.DragObject.Drag(self,self.player,event)
        # Update
        self.all_sprites.update()

    def draw(self):
        # Draw
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        py.display.flip()
