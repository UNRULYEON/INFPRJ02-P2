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

# Initialize pygame
try:
    pg.init()
    logging.info("Pygame initizalized")
except:
    logging.error("Could not initialize pygame")
    logging.error(pg.get_error())
if not pg.font:
    logging.error("FONTS COULD NOT BE LOADED")
if not pg.mixer:
    logging.error("SOUND COULD NOT BE LOADED")
state = True
clock = pg.time.Clock()
fps = 60

# Windows settings
screen_size = width, height = 800, 600
screen_caption = "EduGame"

# Generate screen
pg.display.set_caption(screen_caption)
logging.info("Display caption has been set to: " + str(screen_caption))
screen = pg.display.set_mode(screen_size)
logging.info("Screen size has been set to : " + str(screen_size) + " and is FULLSCREEN")
canvas = pg.display.get_surface()

# Game loop
while state: 
        
    # Set clock speed
    clock.tick(fps)

    # Handle input events
    for event in pg.event.get():

        # KEYUP
        if event.type == pg.KEYUP:
            logging.info("temp")

        # KEYDOWN
        if event.type == pg.KEYDOWN:
            # Check for escape key, when pressed, quit the game
            if event.key == K_ESCAPE:
                logging.info("ESCAPE key was pressed")
                state = False
                logging.info("State of the game has been set to: " + str(state))

            # TOGGLE FULLSCREEN
            elif event.key == K_F12:
                logging.info("Toggle fullscreen")
                pg.display.toggle_fullscreen()

            # W
            elif event.key == K_w or K_UP:
                logging.info("W")
                pg.display.toggle_fullscreen()

            # A
            elif event.key == K_a or K_LEFT:
                logging.info("A")

            # S
            elif event.key == K_s or K_DOWN:
                logging.info("S")

            # D
            elif event.key == K_d or K_UP:
                logging.info("D")

    # MENU
    
            
    # GAME


    # UPDATE SCREEN
    pg.display.update()

# Quit python
logging.info("Quiting EduGame...")
quit()