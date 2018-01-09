import os, sys
import pygame as pg
import MainGame as mg
from pygame.locals import *
import LoadAssets as la

class object(pg.sprite.Sprite):
    # CONSTRUCTOR
    def __init__(self):
        print("INIT OBJECTS")
        pg.sprite.Sprite.__init__(self)
        self.image = la.asset("bookcase.png")
        self.screen = pg.display.get_surface()
