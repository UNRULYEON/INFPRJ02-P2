import os, sys
import logging
import pygame as pg
from pygame.locals import *

# Logging settings
logging.basicConfig(filename="edugame.log", format="%(asctime)s : %(levelname)s : %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)

"""
Logging exapmles

logging.debug("MESSASGE")
logging.info("MESSAGE")
logging.warning("MESSAGE")
"""

logging.info("")
logging.info("--------------------------")
logging.info("")
logging.info("New instance of EduGame.py")

screen_size = width, height = 800, 600
screen_caption = "EduGame"

# DEFINE METHODS
class Player(object):

    size = (50,50)

    def __init__(self, pos):
        self.rect = pg.Rect((0,0), Player.size)
        self.rect.center = pos

    def draw(self, surface):
        surface.fill(pg.Color("red"), self.rect)

class Game(object):

    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.state = True
        self.keys = pg.key.get_pressed()
        self.player = Player(self.screen_rect.center)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.state = False
            elif event.type in (pg.KEYUP, pg.KEYDOWN):
                self.keys = pg.key.get_pressed()

    def render(self):
        self.screen.fill(pg.Color("black"))
        self.player.draw(self.screen)
        pg.display.update()

    def main_loop(self):
        while self.state:
            self.event_loop()
            self.render()
            self.clock.tick(self.fps)

# MAIN LOOP


# INIT GAME
def main():
    pg.init()
    pg.display.set_caption(screen_caption)
    pg.display.set_mode(screen_size)
    Game().main_loop()
    pg.quit()
    sys.exit()  

if __name__ == "__main__":
    main()