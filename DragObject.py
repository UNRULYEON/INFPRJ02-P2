from pygame.locals import *


class DragObject:
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0
        self.dragging = False

    def update(self, event, rect, mask):
        if event.type == MOUSEBUTTONDOWN:
            if self.point_collision(event.pos, rect, mask):
                self.dragging = True
                mx, my = event.pos
                self.offset_x = rect.x - mx
                self.offset_y = rect.y - my
        elif event.type == MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == MOUSEMOTION:
            if self.dragging:
                mx, my = event.pos
                rect.x = mx + self.offset_x
                rect.y = my + self.offset_y
        pass

    def point_collision(self, point, rect, mask):
        x, y = point
        x -= rect.x
        y -= rect.y
        try:
            return mask.get_at((x, y))
        except IndexError:
            return False
