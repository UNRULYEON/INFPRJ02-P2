import pygame as py
from pygame import *

PIECE_SIZE = 63
# Ball class

class Ball(py.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y, spritegroup, grid):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(path).convert_alpha()
        self.image = py.transform.scale(self.image, (PIECE_SIZE, PIECE_SIZE))
        self.mask = py.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.grid = grid
        self.dragging = False
        self.offset_x = None
        self.offset_y = None
        spritegroup.add(self)

    def update(self):
        if not self.dragging:
            self.rect.x = 162 + self.grid[0] * PIECE_SIZE
            self.rect.y = 30 + self.grid[1] * PIECE_SIZE

    def end(self):
        self.kill()
