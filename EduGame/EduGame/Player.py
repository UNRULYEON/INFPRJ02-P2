import os, sys
import logging
import pygame as pg
import MainGame as mg
from pygame.locals import *
import LoadAssets as la

class Player(pg.sprite.Sprite):

    # CONSTRUCTOR
    def __init__(self):
        logging.info("INIT PLAYER")
        print("INIT PLAYER")
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = la.asset("player_down.png")
        self.screen = pg.display.get_surface()
        self.pos = [int(mg.screen_width / 2), int(mg.screen_height / 2)]
        self.width = 50
        self.height = 50
        self.speed_idle = 0
        self.speed_walk = 3
        self.state = "idle"
        self.last_state = "idle"
        self.player_up_ani = ['player_up_walk-1.png','player_up_walk-2.png']
        self.player_down_ani = ['player_down_walk-1.png','player_down_walk-2.png']
        self.player_left_ani = ['player_left_walk-1.png','player_left_walk-2.png']
        self.player_right_ani = ['player_right_walk-1.png','player_right_walk-2.png']
        self.counter = 0
        self.time_counter = 0

    def stop(self):
        self.last_state = self.state
        self.state = "idle"
        self.time_counter = 0
        if self.last_state is str("up"):
            self.image, self.rect = la.asset("player_up.png")
        elif self.last_state is str("down"):
            self.image, self.rect = la.asset("player_down.png")
        elif self.last_state is str("left"):
            self.image, self.rect = la.asset("player_left.png")
        elif self.last_state is str("right"):
            self.image, self.rect = la.asset("player_right.png")
        self.speed = self.speed_idle

    def move_up(self):
        logging.info("UP")
        self.speed = self.speed_walk
        self.state = "up"

    def move_down(self):
        logging.info("DOWN")
        self.speed = self.speed_walk
        self.state = "down"

    def move_left(self):
        logging.info("LEFT")
        self.speed = self.speed_walk
        self.state = "left"

    def move_right(self):
        logging.info("RIGHT")
        self.speed = self.speed_walk
        self.state = "right"

    def render(self, screen):
        if self.state is "up" and (self.pos[1] >= 35):
            self.time_counter += 1
            if self.time_counter <= 7:
                self.image, self.rect = la.asset(self.player_up_ani[0])
            elif self.time_counter >= 7 and self.time_counter <= 14:
                self.image, self.rect = la.asset("player_up.png")
            elif self.time_counter >= 14 and self.time_counter <= 21:
                self.image, self.rect = la.asset(self.player_up_ani[1])
            elif self.time_counter >= 21:
                self.time_counter = 0
            self.pos[1] -= self.speed
        elif self.state is "down" and (self.pos[1] <= 500):
            self.time_counter += 1
            if self.time_counter <= 7:
                self.image, self.rect = la.asset(self.player_down_ani[0])
            elif self.time_counter >= 7 and self.time_counter <= 14:
                self.image, self.rect = la.asset("player_down.png")
            elif self.time_counter >= 14 and self.time_counter <= 21:
                self.image, self.rect = la.asset(self.player_down_ani[1])
            elif self.time_counter >= 21:
                self.time_counter = 0
            self.pos[1] += self.speed
        elif self.state is "left" and (self.pos[0] >= 10):
            self.time_counter += 1
            if self.time_counter <= 7:
                self.image, self.rect = la.asset(self.player_left_ani[0])
            elif self.time_counter >= 7 and self.time_counter <= 14:
                self.image, self.rect = la.asset("player_left.png")
            elif self.time_counter >= 14 and self.time_counter <= 21:
                self.image, self.rect = la.asset(self.player_left_ani[1])
            elif self.time_counter >= 21:
                self.time_counter = 0
            self.pos[0] -= self.speed
        elif self.state is "right" and (self.pos[0] <= 700):
            self.time_counter += 1
            if self.time_counter <= 7:
                self.image, self.rect = la.asset(self.player_right_ani[0])
            elif self.time_counter >= 7 and self.time_counter <= 14:
                self.image, self.rect = la.asset("player_right.png")
            elif self.time_counter >= 14 and self.time_counter <= 21:
                self.image, self.rect = la.asset(self.player_right_ani[1])
            elif self.time_counter >= 21:
                self.time_counter = 0
            self.pos[0] += self.speed
        self.screen.blit(self.image, (self.pos))
        pg.display.update()