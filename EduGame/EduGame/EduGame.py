import os, sys
import logging
import pygame as pg
from pygame.locals import *

# LOGGING SETTINGS
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

# SCREEN SETTINGS
screen_size = width, height = 800, 600
screen_caption = "EduGame"
grid = []
for row in range(20):
    grid.append([])
    for column in range(20):
        grid[row].append(0)



class Player(object):

    # CONSTRUCTOR
    def __init__(self):
        self.pos = [int(width / 2), int(height / 2)]

    # METHODS
    # MOVEMENT
    def move_up(self):
        print("Moving player UP")
        self.pos[1] = self.pos[1]-20

    def move_left(self):
        print("Moving player LEFT")
        self.pos[0] = self.pos[0]-20

    def move_down(self):
        print("Moving player DOWN")
        
        self.pos[1] = self.pos[1]+20

    def move_right(self):
        print("Moving player RIGHT")
        self.pos[0] = self.pos[0]+20

    # DRAW
    def draw(self, screen):
        pg.draw.circle(screen, (255,255,255), self.pos, 20)

class MainMenu(object):

    # CONSTRUCTOR
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.state = True

    # METHODS
    def control(self):
        for event in pg.event.get():

            # KEYUP
            if event.type == pg.KEYUP:
                logging.info("")

            # KEYDOWN
            elif event.type == pg.KEYDOWN:
                # Check for escape key, when pressed, quit the game
                if event.key == K_ESCAPE:
                    logging.info("ESCAPE key was pressed")
                    print("ESCAPE")
                    self.state = False

                # W
                elif event.key == K_w or event.key == K_UP:
                    logging.info("W key was pressed")

                # S
                elif event.key == K_s or event.key == K_DOWN:
                    logging.info("S key was pressed")

    def render(self):
        self.screen.fill(pg.Color("black"))
        pg.display.update()

    def main_loop(self):
        while self.state:
            self.control()
            self.render()
            self.clock.tick(self.fps)

class Game(object):
    
    # CONSTRUCTOR
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.state = True

        # GAME CONSTANTS
        self.level = 0
        self.score = 0

        self.player = Player()
        
    # METHODS
    def control(self):
        for event in pg.event.get():

            # KEYUP
            if event.type == pg.KEYUP:
                logging.info("")

            # KEYDOWN
            elif event.type == pg.KEYDOWN:
                # Check for escape key, when pressed, quit the game
                if event.key == K_ESCAPE:
                    logging.info("ESCAPE key was pressed")
                    print("ESCAPE")
                    self.state = False

                # W
                elif event.key == K_w or event.key == K_UP:
                    logging.info("W key was pressed")
                    self.player.move_up()

                # A
                elif event.key == K_a or event.key == K_LEFT:
                    logging.info("A key was pressed")
                    self.player.move_left()

                # S
                elif event.key == K_s or event.key == K_DOWN:
                    logging.info("S key was pressed")
                    self.player.move_down()

                # D
                elif event.key == K_d or event.key == K_RIGHT:
                    logging.info("D key was pressed")
                    self.player.move_right()

    def set_level(self, lvl):
        self.level = self.level + lvl

    def set_score(self, score):
        self.score = self.score + score

    def render(self):
        self.screen.fill(pg.Color("black"))
        self.player.draw(self.screen)
        pg.display.update()

    def main_loop(self):
        while self.state:
            self.control()
            self.render()
            self.clock.tick(self.fps)

# INIT GAME
def main():
    pg.init()
    pg.font.init()
    pg.display.set_caption(screen_caption)
    pg.display.set_mode(screen_size)
    pg.mouse.set_visible(0)
    MainMenu().main_loop()
    Game().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()