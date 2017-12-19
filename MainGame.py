import os, sys
import logging
import pygame as pg
from pygame.locals import *
from MainMenu import *
from LoadAssets import *
from Player import *
from Objects import *
#from minigames.amar import minigameAmar

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
screen_caption = "School Roamer"

# GAME VARIABLES 
level = 1
completed = 0

# COLORS
white = (255, 255, 255)
red = (255, 0, 0)

# ASSETS
#player, player_rect = la.asset("player_down.png")
bg, bg_rect = la.asset("bg.png")
table_back, table_back_rect = la.asset("table_back.png")
table_front, table_front_rect = la.asset("table_front.png")
board, board_rect = la.asset("board.png")
chair, chair_rect = la.asset("chair.png")
bookcase, bookcase_rect = la.asset("bookcase.png")

class Game(object):
    # CONSTRUCTOR
    def __init__(self):
        logging.info("LOADING GAME")
        print("LOADING GAME")
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.state = True

        self.bg = bg
        self.table_back = table_back
        self.table_front = table_front
        self.board = board
        self.chair = chair
        self.bookcase = bookcase
        
        self.player = Player()

        self.screen.blit(bg, (0, 0))
        pg.display.flip()

    def control(self):
        for event in pg.event.get():

            # QUIT
            if event.type == QUIT:   
                print("ESCAPE")
                self.state = False

            # KEYUP
            if event.type == KEYUP:                    
                # W
                if event.key == K_w or event.key == K_UP:
                    logging.info("W key was released")
                    self.player.stop()
                # S
                if event.key == K_s or event.key == K_DOWN:
                    logging.info("S key was released")
                    self.player.stop()
                # A
                if event.key == K_a or event.key == K_LEFT:
                    logging.info("A key was released")
                    self.player.stop()
                # D
                if event.key == K_d or event.key == K_RIGHT:
                    logging.info("D key was released")
                    self.player.stop()

            # KEYDOWN
            elif event.type == KEYDOWN:
                # Check for escape key, when pressed, quit the game
                if event.key == K_ESCAPE:
                    logging.info("ESCAPE key was pressed")
                    print("ESCAPE")
                    self.state = False
                # W
                if event.key == K_w or event.key == K_UP:
                    logging.info("W key is being held down")
                    self.player.move_up()
                # S
                if event.key == K_s or event.key == K_DOWN:
                    logging.info("S key is being held down")
                    self.player.move_down()
                # A
                if event.key == K_a or event.key == K_LEFT:
                    logging.info("A key is being held down")
                    self.player.move_left()
                # D
                if event.key == K_d or event.key == K_RIGHT:
                    logging.info("D key is being held down")
                    self.player.move_right()
                # SPACE
                if event.key == K_SPACE:
                    logging.info("Space is being held down")
                    self.player.space()

    def render(self):
        self.screen.blit(bg, (0,0))
        self.player.render(self.screen)
        pg.display.flip()
    
    def main_loop(self):
        while self.state:
            pg.event.pump()
            self.control()
            self.render()
            #print(str(self.player.x), str(self.player.y))
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
    pg.key.set_repeat(1, 20)
    MainMenu().main_loop()
    Game().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
