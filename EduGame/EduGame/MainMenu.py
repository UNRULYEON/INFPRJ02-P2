import os, sys
import logging
import pygame as pg
from pygame.locals import *
from MainGame import *
from LoadAssets import *
from DrawText import *

class MainMenu(object):

    # CONSTRUCTOR
    def __init__(self):
        logging.info("[MM] - LOADING MAIN MENU")
        print("[MM] - LOADING MAIN MENU")
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.state = True
        self.draw = DrawText()
        self.font = pg.font.Font(None, 30)
        self.fsize = 16
        self.selected = 1

    # METHODS
    def control(self):
        for event in pg.event.get():

            # QUIT
            if event.type == QUIT:   
                print("ESCAPE")
                pg.quit()
                sys.exit()

            # KEYUP
            if event.type == pg.KEYUP:
                logging.info("")

            # KEYDOWN
            elif event.type == pg.KEYDOWN:
                # Check for escape key, when pressed, quit the game
                if event.key == K_ESCAPE:
                    logging.info("ESCAPE key was pressed")
                    print("ESCAPE")
                    pg.quit()
                    sys.exit()
                
                # ENTER
                elif event.key == K_SPACE:
                    logging.info("SPACE key was pressed")
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
            logging.info("was 1, now 0. Exit is highlighted")
            self.selected = 0
            self.screen.fill(pg.Color("black"))
            self.draw.rtcenter(self.screen, "NEW GAME", 30, None, white, 0, 0, 1)
            self.draw.rtcenter(self.screen, "EXIT", 30, None, white, 0, 50, 1)
            pg.draw.rect(self.screen, red, (screen_width / 2 - 35, screen_height / 2 + 32.5, 70, 35), 2)
            self.draw.rtcenter(self.screen, "SELECT: W AND S", 20, None, white, -100, 200, 1)
            self.draw.rtcenter(self.screen, "CONFIRM: SPACE", 20, None, white, 100, 200, 1)
        elif self.selected == 0:
            self.selected = 1
            self.screen.fill(pg.Color("black"))
            logging.info("was 0, now 1. New Game is highlighted")
            self.draw.rtcenter(self.screen, "NEW GAME", 30, None, white, 0, 0, 1)
            pg.draw.rect(self.screen, red, (screen_width / 2 - 70, screen_height / 2 - 17.5, 140, 35), 2)
            self.draw.rtcenter(self.screen, "EXIT", 30, None, white, 0, 50, 1)
            self.draw.rtcenter(self.screen, "SELECT: W AND S", 20, None, white, -100, 200, 1)
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

        self.draw.rtcenter(self.screen, "SELECT: W AND S", 20, None, white, -100, 200, 1)
        self.draw.rtcenter(self.screen, "CONFIRM: SPACE", 20, None, white, 100, 200, 1)
        pg.display.flip()
        while self.state:
            self.control()
            self.render()
            self.clock.tick(self.fps)