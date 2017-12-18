import os, sys
import time
import logging
import pygame as pg
from pygame.locals import *
import MainGame as mg
from minigames.amar import level1
from random import randint, choice

# LOGGING SETTINGS
logging.basicConfig(filename="minigameAmar.log", format="%(asctime)s : %(levelname)s : %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)

"""
Logging exapmles
logging.debug("MESSASGE")
logging.info("MESSAGE")
logging.warning("MESSAGE")
"""

logging.info("")
logging.info("--------------------------")
logging.info("")
logging.info("New instance of minigameAmar.py")

# SCREEN SETTINGS
screen_caption = "School Roamer - Amar"
# Delete this for prod
screen_size = screen_width, screen_height = 800, 600

def asset(name):
    fullname = os.path.join("assets", name)
    image = pg.image.load(fullname)
    return image, image.get_rect()

class DrawText(object):

    def __init__(self):
        logging.info("INIT DRAW")
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

class Problem(object):

    # CONSTRUCTOR
    def __init__(self):
        self.level = mg.level
        self.completed = mg.completed
        self.draw = DrawText()
        self.screen = pg.display.get_surface()
        self.font = pg.font.Font(None, 30)
        self.fsize = 16    
        print("Player is level: " + str(self.level))
        print("Player has completed " + str(self.completed) + " minigames")
        self.reinit()

    def reinit(self):
        print("test")
        if self.level is 1:
            print("Creating level 1 problem")

            global answer
            global numbers
            global posNum
            global choiceNumbers
            global posNumGuess1
            global posNumGuess2
            numbers = []
            choiceNumbers = []
            a, b, c, sort_answer, answer = level1.gen_problem(self)

            numbers.append(a)
            choiceNumbers.append(a)
            numbers.append(b)
            choiceNumbers.append(b)
            numbers.append(c)
            choiceNumbers.append(c)

            guess1 = choice(choiceNumbers)
            posNumGuess1 = numbers.index(guess1)
            choiceNumbers.remove(guess1)

            guess2 = choice(choiceNumbers)
            posNumGuess2 = numbers.index(guess2)
            choiceNumbers.remove(guess2)

            posNum = numbers.index(choiceNumbers[0])

            logging.info(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(sort_answer) + ", " + str(answer))
            print(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(sort_answer) + ", " + str(answer))
            print("Number the user has to put in the right place: " + str(guess1) + " and " + str(guess2))

        elif self.level is 2:
            print("Creating level 2 problem")
        elif self.level is 3:
            print("Creating level 3 problem")
        elif self.level is 4:
            print("Creating level 4 problem")
        elif self.level is 5:
            print("Creating level 5 problem")

    def control(self):
        for event in pg.event.get():

            # QUIT
            if event.type == QUIT:   
                print("ESCAPE")
                Minigame.state = False

            # MOUSE UP
            if event.type == pg.MOUSEBUTTONUP:             
                logging.info("mouse up")
                print("mouse up")

            # MOUSE DOWN
            if event.type == pg.MOUSEBUTTONDOWN:       
                logging.info("mouse down")
                print("mouse down")

            # KEYDOWN
            elif event.type == KEYDOWN:
                # Check for escape key, when pressed, quit the game
                if event.key == K_ESCAPE:
                    logging.info("ESCAPE key was pressed")
                    print("ESCAPE MINIGAME")
                    Minigame.state = False

    def render(self):
        self.draw.rt(self.screen, "Level: " + str(self.level), 30, None, mg.white, 715, 10, 1)
        if posNum is 0:
            self.draw.rt(self.screen, numbers[posNum], 60, None, mg.white, 300, 300, 1)
            if posNumGuess1 is 1:
                self.draw.rt(self.screen, numbers[posNumGuess1], 60, None, mg.white, 400, 300, 1)
                self.draw.rt(self.screen, numbers[posNumGuess2], 60, None, mg.white, 500, 300, 1)
            if posNumGuess1 is 2:
                self.draw.rt(self.screen, numbers[posNumGuess1], 60, None, mg.white, 500, 300, 1)
                self.draw.rt(self.screen, numbers[posNumGuess2], 60, None, mg.white, 400, 300, 1)
        elif posNum is 1:
            self.draw.rt(self.screen, numbers[posNum], 60, None, mg.white, 400, 300, 1)
            if posNumGuess1 is 0:
                self.draw.rt(self.screen, numbers[posNumGuess1], 60, None, mg.white, 300, 300, 1)
                self.draw.rt(self.screen, numbers[posNumGuess2], 60, None, mg.white, 500, 300, 1)
            if posNumGuess1 is 2:
                self.draw.rt(self.screen, numbers[posNumGuess1], 60, None, mg.white, 500, 300, 1)
                self.draw.rt(self.screen, numbers[posNumGuess2], 60, None, mg.white, 300, 300, 1)
        if posNum is 2:
            self.draw.rt(self.screen, numbers[posNum], 60, None, mg.white, 500, 300, 1)
            if posNumGuess1 is 0:
                self.draw.rt(self.screen, numbers[posNumGuess1], 60, None, mg.white, 300, 300, 1)
                self.draw.rt(self.screen, numbers[posNumGuess2], 60, None, mg.white, 400, 300, 1)
            if posNumGuess1 is 1:
                self.draw.rt(self.screen, numbers[posNumGuess1], 60, None, mg.white, 400, 300, 1)
                self.draw.rt(self.screen, numbers[posNumGuess2], 60, None, mg.white, 300, 300, 1)
                
        self.draw.rt(self.screen, "=       " + str(answer), 60, None, mg.white, 600, 300, 1)
        pg.display.flip()
        
class Minigame(object):

    state = True

    # CONSTRUCTOR
    def __init__(self):
        logging.info("LOADING MINIGAME AMAR")
        print("LOADING MINIGAME AMAR")
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60

        self.problem = Problem()

    def render(self):
        self.screen.fill((12,75,22))
        self.problem.render()
        pg.display.flip()
    
    def main_loop(self):
        Minigame.state = True
        while Minigame.state:
            self.problem.control()
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
    pg.display.set_caption("School Roamer")
    pg.mouse.set_visible(0)

if __name__ == "__main__":
    main()