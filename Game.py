import pygame as py
import sys
import Object as obj
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
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.player.rect.collidepoint(event.pos):
                        self.dragging = True
                        mouse_x, mouse_y = event.pos
                        self.offset_x = self.player.rect.x - mouse_x
                        self.offset_y = self.player.rect.y - mouse_y

            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False

            elif event.type == MOUSEMOTION:
                if self.dragging:
                    mouse_x, mouse_y = event.pos
                    self.player.rect.x = mouse_x + self.offset_x
                    self.player.rect.y = mouse_y + self.offset_y

        # Update
        self.all_sprites.update()

    def draw(self):
        # Draw
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        py.display.flip()
