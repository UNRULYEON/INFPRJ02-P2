import pygame
from DragObject import DragObject
from pygame.locals import *


# Object class
class Object(pygame.sprite.Sprite, DragObject):
    def __init__(self, path, pos_x, pos_y, spritegroup):
        DragObject.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image,( 100, 100))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        spritegroup.add(self)

    def update(self, event):
        DragObject.update(self, event, self.rect, self.mask)
 
