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
screen_size = screen_width, screen_height = 800, 600
screen_caption = "EduGame"
grid = []
for row in range(20):
    grid.append([])
    for column in range(20):
        grid[row].append(0)

# CONSTANTS
# COLORS
white = (255, 255, 255)
red = (255, 0, 0)

class Player(object):

    # CONSTRUCTOR
    def __init__(self):
        logging.info("PLAYER LOADED")
        print("PLAYER LOADED")
        self.pos = [int(screen_width / 2), int(screen_height / 2)]

    # METHODS
    # MOVEMENT
    def move_up(self):
        print("Moving player UP")
        self.pos[1] = self.pos[1]-40

    def move_left(self):
        print("Moving player LEFT")
        self.pos[0] = self.pos[0]-40

    def move_down(self):
        print("Moving player DOWN")
        
        self.pos[1] = self.pos[1]+40

    def move_right(self):
        print("Moving player RIGHT")
        self.pos[0] = self.pos[0]+40

    def draw(self, screen):
        pg.draw.circle(screen, (255,255,255), self.pos, 20)

class Draw(object):

    def __init__(self):
        self.label = ""
        self.size = 12
        self.color = (255, 255, 255)
        self.posx = 0
        self.posy = 0
        self.screen = pg.display.get_surface()

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

class MainMenu(object):

    # CONSTRUCTOR
    def __init__(self):
        logging.info("LOADING MAIN MENU")
        print("LOADING MAIN MENU")
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.state = True
        self.font = pg.font.Font(None, 30)
        self.fsize = 16
        self.draw = Draw()
        self.selected = 1

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
                
                # ENTER
                elif event.key == K_SPACE:
                    logging.info("ENTER key was pressed")
                    self.mm_confirm(self.selected)

                # W
                elif event.key == K_w or event.key == K_UP:
                    logging.info("W key was pressed")
                    self.mm_selector()


                # S
                elif event.key == K_s or event.key == K_DOWN:
                    logging.info("S key was pressed")
                    self.mm_selector()


    def mm_render(self):

        pg.display.flip()

    def mm_selector(self):
        if self.selected == 1:
            print("was 1, now 0. Exit is highlighted")
            self.selected = 0
            self.screen.fill(pg.Color("black"))
            self.draw.rtcenter(self.screen, "NEW GAME", 30, None, white, 0, 0, 1)
            self.draw.rtcenter(self.screen, "EXIT", 30, None, white, 0, 50, 1)
            pg.draw.rect(self.screen, red, (screen_width / 2 - 35, screen_height / 2 + 32.5, 70, 35), 2)
            self.draw.rtcenter(self.screen, "SELECT: UP AND DOWN", 20, None, white, -100, 200, 1)
            self.draw.rtcenter(self.screen, "CONFIRM: SPACE", 20, None, white, 100, 200, 1)
        elif self.selected == 0:
            self.selected = 1
            self.screen.fill(pg.Color("black"))
            print("was 0, now 1. New Game is highlighted")
            self.draw.rtcenter(self.screen, "NEW GAME", 30, None, white, 0, 0, 1)
            pg.draw.rect(self.screen, red, (screen_width / 2 - 70, screen_height / 2 - 17.5, 140, 35), 2)
            self.draw.rtcenter(self.screen, "EXIT", 30, None, white, 0, 50, 1)
            self.draw.rtcenter(self.screen, "SELECT: UP AND DOWN", 20, None, white, -100, 200, 1)
            self.draw.rtcenter(self.screen, "CONFIRM: SPACE", 20, None, white, 100, 200, 1)

    def mm_confirm(self, action):
        if action == 0:
            logging.info("EXIT GAME")
            pg.quit()
            sys.exit()

        elif action == 1:
            logging.info("NEW GAME")
            self.state = False

        else:
            logging.info("SOMETHING WENT WRONG")
            print("SOMETHING WENT WRONG")

    def render(self):
        self.mm_render()
        pg.display.update()

    def main_loop(self):
        self.draw.rtcenter(self.screen, "NEW GAME", 30, None, white, 0, 0, 1)
        pg.draw.rect(self.screen, red, (screen_width / 2 - 70, screen_height / 2 - 17.5, 140, 35), 2)
        #pg.draw.line(self.screen, red, (343, 310), (457, 310), 2)

        self.draw.rtcenter(self.screen, "EXIT", 30, None, white, 0, 50, 1)
        #pg.draw.rect(self.screen, red, (screen_width / 2 - 35, screen_height / 2 + 32.5, 70, 35), 2)
        #pg.draw.line(self.screen, red, (378, 360), (422, 360), 2)

        self.draw.rtcenter(self.screen, "SELECT: UP AND DOWN", 20, None, white, -100, 200, 1)
        self.draw.rtcenter(self.screen, "CONFIRM: SPACE", 20, None, white, 100, 200, 1)
        pg.display.flip()
        while self.state:
            self.control()
            self.render()
            self.clock.tick(self.fps)

class Game(object):
    
    # CONSTRUCTOR
    def __init__(self):
        logging.info("LOADING GAME")
        print("LOADING GAME")
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
    # FULLSCREEN MODE
    # pg.display.set_mode(screen_size, pg.FULLSCREEN)
    pg.mouse.set_visible(0)
    MainMenu().main_loop()
    Game().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()