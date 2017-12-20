import logging
import pygame as pg
import MainGame as mg
from pygame.locals import *
import pyganim

class Player(object):

    # CONSTRUCTOR
    def __init__(self):
        logging.info("INIT PLAYER")
        print("INIT PLAYER")
        pg.sprite.Sprite.__init__(self)
        self.screen = pg.display.get_surface()
        self.speed = 7
        self.x = ((mg.screen_width // 2) - 48)
        self.y = ((mg.screen_height // 2) + 100)
        self.state = "idle"
        self.last_state = "start"

        #ANIMATIONs
        self.up_standing = pg.image.load("assets/player_up.png")
        self.down_standing = pg.image.load("assets/player_down.png")
        self.left_standing = pg.image.load("assets/player_left.png")
        self.right_standing = pg.image.load("assets/player_right.png")
        self.upAnim = pyganim.PygAnimation([("assets/player_up_walk-1.png", .2),
                                         ("assets/player_up.png", .1),
                                         ("assets/player_up_walk-2.png", .2)])

        self.downAnim = pyganim.PygAnimation([("assets/player_down_walk-1.png", .2),
                                         ("assets/player_down.png", .1),
                                         ("assets/player_down_walk-2.png", .2)])

        self.leftAnim = pyganim.PygAnimation([("assets/player_left_walk-1.png", .2),
                                        ("assets/player_left.png", .1),
                                         ("assets/player_left_walk-2.png", .2)])

        self.rightAnim = pyganim.PygAnimation([("assets/player_right_walk-1.png", .2),
                                         ("assets/player_right.png", .1),
                                         ("assets/player_right_walk-2.png", .2)])

    def stop(self):
        self.state = "idle"
        self.upAnim.stop()
        self.downAnim.stop()
        self.leftAnim.stop()
        self.rightAnim.stop()
        
    def move_up(self):
        if self.y >= 300:
            self.y -= self.speed
        self.upAnim.play()
        self.state = self.last_state = "moveup"

    def move_down(self):
        if self.y <= 497:
            self.y += self.speed
        self.downAnim.play()
        self.state = self.last_state = "movedown"

    def move_left(self):
        if self.x >= 2:
            self.x -= self.speed
        self.leftAnim.play()
        self.state = self.last_state = "moveleft"

    def move_right(self):
        if self.x <=702:
            self.x += self.speed
        self.rightAnim.play()
        self.state = self.last_state = "moveright"

    def space(self):
        if self.x > 230 and self.x < 275 and self.y > 250 and self.y < 320 and mg.minigame_vlad is False:
            print(str(self.x), str(self.y))
            #LAUNCH MINIGAME 2
            logging.info("LAUNCHING GAME 2")
            print("LAUNCHING GAME 2")
            
            self.upAnim.stop()
            self.downAnim.stop()
            self.leftAnim.stop()
            self.rightAnim.stop()
        if self.x > 330 and self.x < 380 and self.y > 250 and self.y < 320 and mg.minigame_amar is False:
            print(str(self.x), str(self.y))
            #LAUNCH MINIGAME 3
            logging.info("LAUNCHING GAME 3")
            print("LAUNCHING GAME 3")
            
            self.upAnim.stop()
            self.downAnim.stop()
            self.leftAnim.stop()
            self.rightAnim.stop()
        if self.x > 430 and self.x < 480 and self.y > 250 and self.y < 320 and mg.minigame_armand is False:
            print(str(self.x), str(self.y))
            #LAUNCH MINIGAME 4
            logging.info("LAUNCHING GAME 4")
            print("LAUNCHING GAME 4")

            self.upAnim.stop()
            self.downAnim.stop()
            self.leftAnim.stop()
            self.rightAnim.stop()


    def render(self, screen):
        if self.state is "idle":
            if self.last_state is "moveup":
                self.screen.blit(self.up_standing, (self.x, self.y))
            elif self.last_state is "movedown":
                self.screen.blit(self.down_standing, (self.x, self.y))
            elif self.last_state is "moveleft":
                self.screen.blit(self.left_standing, (self.x, self.y))
            elif self.last_state is "moveright":
                self.screen.blit(self.right_standing, (self.x, self.y))
            elif self.last_state is "start":
                self.screen.blit(self.down_standing, (self.x, self.y))
        elif self.state is "moveup":
            self.upAnim.blit(self.screen, (self.x, self.y))
        elif self.state is "movedown":
            self.downAnim.blit(self.screen, (self.x, self.y))
        elif self.state is "moveleft":
            self.leftAnim.blit(self.screen, (self.x, self.y))
        elif self.state is "moveright":
            self.rightAnim.blit(self.screen, (self.x, self.y))

