import os, sys
import pygame as pg
from pygame.locals import *
from MainMenu import *

class DrawText(object):

    def __init__(self):
        self.label = ""
        self.size = 12
        self.color = (255, 255, 255)
        self.posx = 0
        self.posy = 0
        self.screen = pg.display.get_surface()
        self.grid_width = 50
        self.grid_height = 50

    def rt(self, tscreen, tlabel, tsize, tfont, tcolor, tposx, tposy, aa):
        self.font = pg.font.Font(tfont, tsize)
        self.label = str(tlabel)
        self.label = self.font.render(self.label, aa, tcolor)
        tscreen.blit(self.label, (tposx, tposy))

    def rtcenter(self, tscreen, tlabel, tsize, tfont, tcolor, tposx, tposy, aa):
        self.font = pg.font.Font(tfont, tsize)
        self.label = str(tlabel)
        self.label = self.font.render(self.label, aa, tcolor)
        self.label_center = self.label.get_rect(center=(screen_width / 2 + tposx, screen_height / 2 + tposy))
        tscreen.blit(self.label, self.label_center)