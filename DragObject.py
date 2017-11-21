import pygame as py
from pygame.locals import *

class DragObject:
    def __init__(self):
    	pass
    def Update(self):
        pass
    def Drag(self, obj, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if obj.rect.collidepoint(event.pos):
                    self.dragging = True
                    mx, my = event.pos
                    self.offset_x = obj.rect.x - mx
                    self.offset_y = obj.rect.y - my

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

        elif event.type == MOUSEMOTION:
            if self.dragging:
                mx, my = event.pos
                obj.rect.x = mx + self.offset_x
                obj.rect.y = my + self.offset_y

