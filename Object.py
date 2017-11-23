import pygame
from pygame.locals import *


# Object class
class Object(pygame.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.offset_x = 0
        self.offset_y = 0
        self.dragging = False

    def update(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                mx, my = event.pos
                self.offset_x = self.rect.x - mx
                self.offset_y = self.rect.y - my
        elif event.type == MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == MOUSEMOTION:
            if self.dragging:
                mx, my = event.pos
                self.rect.x = mx + self.offset_x
                self.rect.y = my + self.offset_y

    def point_collsion(self, point):
        x, y = point
        x -= self.rect.x
        y -= self.rect.y
        try:
            return self.mask.get_at((x, y))
        except IndexError:
            return False


