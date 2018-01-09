import os, sys
import pygame as pg
from pygame.locals import *
from LoadAssets import *
from Player import *
from DrawText import *
from Objects import *

# SCREEN SETTINGS
screen_size = screen_width, screen_height = 800, 600
screen_caption = "School Roamer"

# COLORS
white = (255, 255, 255)

# ASSETS
bg, bg_rect = la.asset("bg.png")


class Game(object):

    # CONSTRUCTOR
    def __init__(self):
        print("LOADING GAME")
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.state = True

        self.bg = bg
        
        self.player = Player()

        self.draw = DrawText()
        self.font = pg.font.SysFont("comicsansms", 30)
        self.fsize = 16

        self.screen.blit(bg, (0, 0))

        # GAME VARIABLES

        self.level = 1
        self.minigame_vlad = False
        self.minigame_amar = False
        self.minigame_armand = False

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
                    self.player.stop()
                # S
                if event.key == K_s or event.key == K_DOWN:
                    self.player.stop()
                # A
                if event.key == K_a or event.key == K_LEFT:
                    self.player.stop()
                # D
                if event.key == K_d or event.key == K_RIGHT:
                    self.player.stop()

            # KEYDOWN
            elif event.type == KEYDOWN:
                # Check for escape key, when pressed, quit the game
                if event.key == K_ESCAPE:
                    print("ESCAPE")
                    self.state = False
                # W
                if event.key == K_w or event.key == K_UP:
                    self.player.move_up()
                # S
                if event.key == K_s or event.key == K_DOWN:
                    self.player.move_down()
                # A
                if event.key == K_a or event.key == K_LEFT:
                    self.player.move_left()
                # D
                if event.key == K_d or event.key == K_RIGHT:
                    self.player.move_right()
                # SPACE
                if event.key == K_SPACE:
                    self.player.space()
                if event.key == K_q:
                    print("Level: " + str(self.level))
                    print("Vlad: " + str(self.minigame_vlad))
                    print("Amar: " + str(self.minigame_amar))
                    print("Armand: " + str(self.minigame_armand))

    def check(self):
        if self.minigame_vlad and self.minigame_amar and self.minigame_armand:
            self.level += 1
            self.minigame_vlad = self.minigame_amar = self.minigame_armand = False
        if self.level is 5:
            pg.quit()
            sys.exit()

    def getMinigameAmar(self):
        self.minigame_amar = self.minigame_amar
        return self.minigame_amar

    def setMinigameAmar(self, boolean):
        self.minigame_amar = boolean

    def render(self):
        self.screen.blit(bg, (0,0))

        self.draw.rtcenter(self.screen, "Level: " + str(self.level), 30, None, white, 355, -280, 1)
        if self.player.x > 230 and self.player.x < 275 and self.player.y > 250 and self.player.y < 320:
            # MINIGAME 1
            # Name minigame
            self.draw.rtcenter(self.screen, "MINIGAME VLAD", 40, None, white, 0, -240, 1)

            # Completed?

            if self.minigame_vlad is True:
                self.draw.rtcenter(self.screen, "You've already completed this minigame!", 30, None, white, 0, -210, 1)
                self.draw.rtcenter(self.screen, "Complete the other minigames to continue to the next level", 30, None, white, 0, -190, 1)

            # How to play
            self.draw.rtcenter(self.screen, "", 30, None, white, 0, -160, 1)

            # Press space to enter
            self.draw.rtcenter(self.screen, "Press SPACE to enter", 30, None, white, 0, -50, 1)

        if self.player.x > 330 and self.player.x < 380 and self.player.y > 250 and self.player.y < 320:
            # MINIGAME 2
            # Name minigame
            self.draw.rtcenter(self.screen, "MINIGAME AMAR", 40, None, white, 0, -240, 0)

            # Completed?
            if self.minigame_amar is True:
                self.draw.rtcenter(self.screen, "You've already completed this minigame!", 30, None, white, 0, -210, 1)
                self.draw.rtcenter(self.screen, "Complete the other minigames to continue to the next level", 30, None, white, 0, -190, 1)

            # How to play
            self.draw.rtcenter(self.screen, "Fill in the correct numbers before the timer runs out", 30, None, white, 0, -160, 1)

            # Press space to enter
            self.draw.rtcenter(self.screen, "Press SPACE to enter", 30, None, white, 0, -50, 0)

        if self.player.x > 430 and self.player.x < 480 and self.player.y > 250 and self.player.y < 320:
            # MINIGAME 3
            # Name minigame
            self.draw.rtcenter(self.screen, "MINIGAME ARMAND", 40, None, white, 0, -240, 0)

            # Completed?

            if self.minigame_armand is True:
                self.draw.rtcenter(self.screen, "You've already completed this minigame!", 30, None, white, 0, -210, 1)
                self.draw.rtcenter(self.screen, "Complete the other minigames to continue to the next level", 30, None, white, 0, -190, 1)

            # How to play
            self.draw.rtcenter(self.screen, "", 30, None, white, 0, -160, 1)

            # Press space to enter
            self.draw.rtcenter(self.screen, "Press SPACE to enter", 30, None, white, 0, -50, 0)

        self.player.render(self.screen)
        pg.display.flip()
    
    def main_loop(self):
        while self.state:
            pg.event.pump()
            self.control()
            self.check()
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
    pg.key.set_repeat(1, 20)
    #MainMenu().main_loop()
    Game().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()