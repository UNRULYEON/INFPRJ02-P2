import os, sys
import logging
import pygame as pg
from pygame.locals import *


# LOGGING SETTINGS
logging.basicConfig(filename="mg-amar.log", format="%(asctime)s : %(levelname)s : %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)

"""
Logging exapmles
logging.debug("MESSASGE")
logging.info("MESSAGE")
logging.warning("MESSAGE")
"""

logging.info("")
logging.info("--------------------------")
logging.info("")
logging.info("New instance of mg-amar.py")

# SCREEN SETTINGS
screen_caption = "School Roamer - Amar"
# Delete this for prod
screen_size = screen_width, screen_height = 800, 600

class Minigame(object):
    # CONSTRUCTOR
    def __init__(self):
        logging.info("LOADING MINIGAME AMAR")
        print("LOADING MINIGAME AMAR")
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.state = True

    def control(self):
        for event in pg.event.get():

            # QUIT
            if event.type == QUIT:   
                print("ESCAPE")
                self.state = False

            # KEYUP
            if event.type == KEYUP:                    
                logging.info("key up")

            # KEYDOWN
            elif event.type == KEYDOWN:
                # Check for escape key, when pressed, quit the game
                if event.key == K_ESCAPE:
                    logging.info("ESCAPE key was pressed")
                    print("ESCAPE")
                    self.state = False

    def render(self):
        pg.display.flip()
    
    def main_loop(self):
        while self.state:
            self.control()
            self.render()
            self.clock.tick(self.fps)

# INIT MINIGAME
def main():
    pg.init()
    pg.font.init()
    pg.display.set_caption(screen_caption)
    # Delete this for prod
    pg.display.set_mode(screen_size)
    # FULLSCREEN MODE
    # pg.display.set_mode(screen_size, pg.FULLSCREEN)
    pg.mouse.set_visible(1)
    pg.key.set_repeat(500, 30)
    Minigame().main_loop()
    pg.quit()

if __name__ == "__main__":
    main()