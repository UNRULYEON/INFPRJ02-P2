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
        self.player = Object("Resources/MM.png", 0, 0,self.all_sprites)
        self.player2 = Object("Resources/MM.png", 300, 300,self.all_sprites)
        self.player3 = Object("Resources/ball.png", 200,300, self.all_sprites)
        
    def update(self, tick_rate):
        # Events
        self.clock.tick(tick_rate)
        for event in py.event.get():
            if event.type == QUIT:
                sys.exit()
            self.all_sprites.update(event)
        # Update

    def draw(self):
        # Draw
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        py.display.flip()
