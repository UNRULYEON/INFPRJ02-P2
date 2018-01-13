from pygame.locals import *
import os, sys, math
import logging
import pygame
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
levelComplete = 0
class Sticky(pygame.sprite.Sprite):
    # Methods
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Starts the parent's constructor

        self.sticky_image = pygame.image.load('minigames/armand/assets/sn.png')
        self.image = self.sticky_image

        # Sets the stickynote's rect
        self.rect = self.image.get_rect()

        # Set the stickynote's start location
        self.rect.x = 0
        self.rect.y = 0

class Main():
        def __init__(self, level):
            self.wrong = False
            self.gameover = False
            self.correct = False
            self.currentLevel = level
            self.win_done = 0
            self.lose_done = 0
            self.sticky1 = Sticky()
            self.sticky2 = Sticky()
            self.sticky3 = Sticky()
            self.sticky4 = Sticky()
            # render text
            self.screen = pygame.display.get_surface()
            self.rect1 = pygame.draw.rect(self.screen, white, (80, 375, 30, 30))
            self.rect2 = pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 128), (280, 375, 30, 30))
            self.rect3 = pygame.draw.rect(self.screen, white, (480, 375, 30, 30))
            self.rect4 = pygame.draw.rect(self.screen, white, (680, 375, 30, 30))
            self.myfont = pygame.font.SysFont("comicsansms", 25)
            self.myfont2 = pygame.font.SysFont("comicsansms", 20)
            self.label1 = self.myfont2.render("Appel", 1, (0, 0, 0))
            self.label2 = self.myfont2.render("Kiwi", 1, (0, 0, 0))
            self.label3 = self.myfont2.render("Mango", 1, (0, 0, 0))
            self.label4 = self.myfont2.render("Peer", 1, (0, 0, 0))
            self.answer1 = self.label1.get_rect(center=self.sticky1.rect.center)
            self.answer2 = self.label2.get_rect(center=self.sticky2.rect.center)
            self.answer3 = self.label3.get_rect(center=self.sticky3.rect.center)
            self.answer4 = self.label4.get_rect(center=self.sticky4.rect.center)
            self.answer1.x = 80
            self.answer1.y = 365
            self.sticky1.rect.x = 55
            self.sticky1.rect.y = 335
            self.answer2.x = 280
            self.answer2.y = 365
            self.sticky2.rect.x = 255
            self.sticky2.rect.y = 335
            self.answer4.x = 680
            self.answer4.y = 365
            self.sticky4.rect.x = 655
            self.sticky4.rect.y = 335
            self.answer3.x = 480
            self.answer3.y = 365
            self.sticky3.rect.x = 455
            self.sticky3.rect.y = 335
            self.answer1_draging = False
            self.answer2_draging = False
            self.answer3_draging = False
            self.answer4_draging = False
            self.correct_answer = None
            self.label = None
            self.gameover_label = self.myfont.render("GAMEOVER", 1, (0, 0, 0))
            self.correct_label = self.myfont.render("CORRECT", 1, (0, 0, 0))

            self.myimage = pygame.image.load("minigames/armand/assets/bg.png")
            self.stickynote = pygame.image.load("minigames/armand/assets/sn.png")

            self.imagerect = self.myimage.get_rect()
            self.start_ticks = pygame.time.get_ticks()

        def levels(self):
            level = self.currentLevel
            vraag1 = randint(1, 10)
            vraag = vraag1
            if level == 1 and vraag1 == 1:
                    self.label = self.myfont.render("Vul aan: De ___ valt niet ver van de boom", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Appel", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Kiwi", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Bes", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Peer", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 1 and vraag1 == 2:
                    self.label = self.myfont.render("Vul aan: Wie de ___ past, trekt hem aan", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Sok", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Schoen", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Laars", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Hoed", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 1 and vraag1 == 3:
                    self.label = self.myfont.render("Vul aan: Iemand een ___ zetten", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Hak", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Stap", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Sprong", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Thee", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 1 and vraag1 == 4:
                    self.label = self.myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Loon", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Zoontje", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Plooitje", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Boontje", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 1 and vraag1 == 5:
                    self.label = self.myfont.render("Vul aan: Zo glad als een ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Koe", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Meer", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Aal", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Aap", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 1 and vraag1 == 6:
                    self.label = self.myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Ja", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Nee", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("C", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("D", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 1 and vraag1 == 7:
                    self.label = self.myfont.render("Vul aan: Niet geschoten is altijd ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Mis", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Dom", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nee", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Ja", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 1 and vraag1 == 8:
                    self.label = self.myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Een", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Het", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Zijn", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("De", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 1 and vraag1 == 9:
                    self.label = self.myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nier", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 1 and vraag1 == 10:
                    self.label = self.myfont.render("Vul aan: Jong geleerd, ___ gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Niet", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer3

            if level == 2 and vraag1 == 1:
                    self.label = self.myfont.render("Vul aan: De ___ valt niet ver van de boom", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Appel", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Kiwi", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Bes", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Peer", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 2 and vraag1 == 2:
                    self.label = self.myfont.render("Vul aan: Wie de ___ past, trekt hem aan", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Sok", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Schoen", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Laars", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Hoed", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 2 and vraag1 == 3:
                    self.label = self.myfont.render("Vul aan: Iemand een ___ zetten", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Hak", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Stap", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Sprong", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Thee", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 2 and vraag1 == 4:
                    self.label = self.myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Loon", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Zoontje", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Plooitje", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Boontje", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 2 and vraag1 == 5:
                    self.label = self.myfont.render("Vul aan: Zo glad als een ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Koe", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Meer", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Aal", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Aap", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 2 and vraag1 == 6:
                    self.label = self.myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Ja", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Nee", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("C", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("D", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 2 and vraag1 == 7:
                    self.label = self.myfont.render("Vul aan: Niet geschoten is altijd ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Mis", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Dom", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nee", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Ja", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 2 and vraag1 == 8:
                    self.label = self.myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Een", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Het", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Zijn", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("De", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 2 and vraag1 == 9:
                    self.label = self.myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nier", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 2 and vraag1 == 10:
                    self.label = self.myfont.render("Vul aan: Jong geleerd, ___ gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Niet", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer3

            if level == 3 and vraag1 == 1:
                    self.label = self.myfont.render("Vul aan: De ___ valt niet ver van de boom", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Appel", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Kiwi", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Bes", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Peer", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 3 and vraag1 == 2:
                    self.label = self.myfont.render("Vul aan: Wie de ___ past, trekt hem aan", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Sok", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Schoen", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Laars", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Hoed", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 3 and vraag1 == 3:
                    self.label = self.myfont.render("Vul aan: Iemand een ___ zetten", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Hak", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Stap", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Sprong", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Thee", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 3 and vraag1 == 4:
                    self.label = self.myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Loon", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Zoontje", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Plooitje", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Boontje", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 3 and vraag1 == 5:
                    self.label = self.myfont.render("Vul aan: Zo glad als een ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Koe", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Meer", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Aal", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Aap", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 3 and vraag1 == 6:
                    self.label = self.myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Ja", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Nee", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("C", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("D", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 3 and vraag1 == 7:
                    self.label = self.myfont.render("Vul aan: Niet geschoten is altijd ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Mis", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Dom", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nee", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Ja", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 3 and vraag1 == 8:
                    self.label = self.myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Een", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Het", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Zijn", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("De", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 3 and vraag1 == 9:
                    self.label = self.myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nier", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 3 and vraag1 == 10:
                    self.label = self.myfont.render("Vul aan: Jong geleerd, ___ gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Niet", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer3

            if level == 4 and vraag1 == 1:
                    self.label = self.myfont.render("Vul aan: De ___ valt niet ver van de boom", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Appel", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Kiwi", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Bes", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Peer", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 4 and vraag1 == 2:
                    self.label = self.myfont.render("Vul aan: Wie de ___ past, trekt hem aan", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Sok", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Schoen", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Laars", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Hoed", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 4 and vraag1 == 3:
                    self.label = self.myfont.render("Vul aan: Iemand een ___ zetten", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Hak", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Stap", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Sprong", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Thee", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 4 and vraag1 == 4:
                    self.label = self.myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Loon", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Zoontje", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Plooitje", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Boontje", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 4 and vraag1 == 5:
                    self.label = self.myfont.render("Vul aan: Zo glad als een ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Koe", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Meer", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Aal", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Aap", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 4 and vraag1 == 6:
                    self.label = self.myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Ja", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Nee", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("C", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("D", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 4 and vraag1 == 7:
                    self.label = self.myfont.render("Vul aan: Niet geschoten is altijd ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Mis", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Dom", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nee", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Ja", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 4 and vraag1 == 8:
                    self.label = self.myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Een", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Het", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Zijn", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("De", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 4 and vraag1 == 9:
                    self.label = self.myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nier", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 4 and vraag1 == 10:
                    self.label = self.myfont.render("Vul aan: Jong geleerd, ___ gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Niet", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer3

            if level == 5 and vraag1 == 1:
                    self.label = self.myfont.render("Vul aan: Beter Laat dan ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Nooit", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Niet", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nu", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Dan", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 5 and vraag1 == 2:
                    self.label = self.myfont.render("Vul aan: Nood breekt ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Dat", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Nood", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Dit", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wet", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 5 and vraag1 == 3:
                    self.label = self.myfont.render("Vul aan: ___ breekt wet", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Nood", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Dit", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Hij", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Dat", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 5 and vraag1 == 4:
                    self.label = self.myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Loon", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Zoontje", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Plooitje", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Boontje", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 5 and vraag1 == 5:
                    self.label = self.myfont.render("Vul aan: Zo glad als een ___", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Koe", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Meer", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Aal", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Aap", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 5 and vraag1 == 6:
                    self.label = self.myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Ja", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Nee", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("C", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("D", 1, (0, 0, 0))
                    self.correct_answer = self.answer4
            elif level == 5 and vraag1 == 7:
                    self.label = self.myfont.render("Vul aan:  Zo lang er ___ is, is er hoop", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Eten", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Leven", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Vrede", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Dat", 1, (0, 0, 0))
                    self.correct_answer = self.answer1
            elif level == 5 and vraag1 == 8:
                    self.label = self.myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Een", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Het", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Zijn", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("De", 1, (0, 0, 0))
                    self.correct_answer = self.answer3
            elif level == 5 and vraag1 == 9:
                    self.label = self.myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Nier", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer2
            elif level == 5 and vraag1 == 10:
                    self.label = self.myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0, 0, 0))
                    self.label1 = self.myfont2.render("Jong", 1, (0, 0, 0))
                    self.label2 = self.myfont2.render("Niet", 1, (0, 0, 0))
                    self.label3 = self.myfont2.render("Oud", 1, (0, 0, 0))
                    self.label4 = self.myfont2.render("Wel", 1, (0, 0, 0))
                    self.correct_answer = self.answer3

        def text(self, x, y):
                self.screen.blit(self.label, (x, y))

        def update(self):
                global levelComplete
                timer_label = None
                while not self.wrong:
                        seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000  # calculate how many seconds
                        second = int(seconds)

                        if self.currentLevel == 1:
                                timer_label = self.myfont.render("Tijd: " + str(12 - second), 1, (0, 0, 0))
                                if seconds > 12 and self.correct == False:  # if more than 12 seconds close the game
                                        self.gameover = True
                        elif self.currentLevel == 2:
                                timer_label = self.myfont.render("Tijd: " + str(10 - second), 1, (0, 0, 0))
                                if seconds > 10 and self.correct == False:  # if more than 10 seconds close the game
                                        self.gameover = True
                        elif self.currentLevel == 3:
                                timer_label = self.myfont.render("Tijd: " + str(8 - second), 1, (0, 0, 0))
                                if seconds > 8 and self.correct == False:  # if more than 8 seconds close the game
                                        self.gameover = True
                        elif self.currentLevel == 4:
                                timer_label = self.myfont.render("Tijd: " + str(6 - second), 1, (0, 0, 0))
                                if seconds > 6 and self.correct == False:  # if more than 6 seconds close the game
                                        self.gameover = True
                        elif self.currentLevel == 5:
                                timer_label = self.myfont.render("Tijd: " + str(4 - second), 1, (0, 0, 0))
                                if seconds > 4 and self.correct == False:  # if more than 4 seconds close the game
                                        self.gameover = True

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        self.wrong = True
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.button == 1:
                                                if self.answer1.collidepoint(event.pos):
                                                        self.answer1_draging = True
                                                        test1_dragging = True
                                                        mouse_x, mouse_y = event.pos
                                                        self.offset_x = self.answer1.x - mouse_x
                                                        self.offset_y = self.answer1.y - mouse_y
                                                        offset_x = self.sticky1.rect.x - mouse_x
                                                        offset_y = self.sticky1.rect.y - mouse_y
                                                elif self.answer2.collidepoint(event.pos):
                                                        self.answer2_draging = True
                                                        mouse_x, mouse_y = event.pos
                                                        self.offset_x = self.answer2.x - mouse_x
                                                        self.offset_y = self.answer2.y - mouse_y
                                                        offset_x = self.sticky2.rect.x - mouse_x
                                                        offset_y = self.sticky2.rect.y - mouse_y
                                                elif self.answer3.collidepoint(event.pos):
                                                        self.answer3_draging = True
                                                        mouse_x, mouse_y = event.pos
                                                        self.offset_x = self.answer3.x - mouse_x
                                                        self.offset_y = self.answer3.y - mouse_y
                                                        offset_x = self.sticky3.rect.x - mouse_x
                                                        offset_y = self.sticky3.rect.y - mouse_y
                                                elif self.answer4.collidepoint(event.pos):
                                                        self.answer4_draging = True
                                                        mouse_x, mouse_y = event.pos
                                                        self.offset_x = self.answer4.x - mouse_x
                                                        self.offset_y = self.answer4.y - mouse_y
                                                        offset_x = self.sticky4.rect.x - mouse_x
                                                        offset_y = self.sticky4.rect.y - mouse_y
                                elif event.type == pygame.MOUSEBUTTONUP:
                                        if event.button == 1:
                                                if self.answer1_draging:
                                                        if answerRect.x <= self.answer1.x <= answerRect.x + 75 and answerRect.y <= self.answer1.y <= answerRect.y + 75:
                                                                if self.correct_answer == self.answer1:
                                                                        self.answer1_draging = False
                                                                        print('Correct')
                                                                        self.correct = True
                                                                else:
                                                                        self.answer1.x = 80
                                                                        self.answer1.y = 365
                                                                        self.sticky1.rect.x = 55
                                                                        self.sticky1.rect.y = 335
                                                                        self.answer1_draging = False
                                                                        print('Wrong')
                                                                        self.gameover = True
                                                        else:
                                                                self.answer1.x = 80
                                                                self.answer1.y = 365
                                                                self.sticky1.rect.x = 55
                                                                self.sticky1.rect.y = 335
                                                                self.answer1_draging = False
                                                elif self.answer2_draging:
                                                        if answerRect.x <= self.answer2.x <= answerRect.x + 75 and answerRect.y <= self.answer2.y <= answerRect.y + 75:
                                                                if self.correct_answer == self.answer2:
                                                                        self.answer2_draging = False
                                                                        print('Correct')
                                                                        self.correct = True
                                                                else:
                                                                        self.answer2.x = 280
                                                                        self.answer2.y = 365
                                                                        self.sticky2.rect.x = 255
                                                                        self.sticky2.rect.y = 335
                                                                        self.answer2_draging = False
                                                                        print('Wrong')
                                                                        self.gameover = True
                                                        else:
                                                                self.answer2.x = 280
                                                                self.answer2.y = 365
                                                                self.sticky2.rect.x = 255
                                                                self.sticky2.rect.y = 335
                                                                self.answer2_draging = False
                                                elif self.answer3_draging:
                                                        if answerRect.x <= self.answer3.x <= answerRect.x + 75 and answerRect.y <= self.answer3.y <= answerRect.y + 75:
                                                                if self.correct_answer == self.answer3:
                                                                        self.answer3_draging = False
                                                                        print('Correct')
                                                                        self.correct = True
                                                                else:
                                                                        self.answer3.x = 480
                                                                        self.answer3.y = 365
                                                                        self.sticky3.rect.x = 455
                                                                        self.sticky3.rect.y = 335
                                                                        self.answer3_draging = False
                                                                        print('Wrong')
                                                                        self.gameover = True
                                                        else:
                                                                self.answer3.x = 480
                                                                self.answer3.y = 365
                                                                self.sticky3.rect.x = 455
                                                                self.sticky3.rect.y = 335
                                                                self.answer3_draging = False

                                                elif self.answer4_draging:
                                                        if answerRect.x <= self.answer4.x <= answerRect.x + 75 and answerRect.y <= self.answer4.y <= answerRect.y + 75:
                                                                if self.correct_answer == self.answer4:
                                                                        self.answer4_draging = False
                                                                        print('Correct')
                                                                        self.correct = True
                                                                else:
                                                                        self.answer4.x = 680
                                                                        self.answer4.y = 365
                                                                        self.sticky4.rect.x = 655
                                                                        self.sticky4.rect.y = 335
                                                                        self.answer4_draging = False
                                                                        print('Wrong')
                                                                        self.gameover = True
                                                        else:
                                                                self.answer4.x = 680
                                                                self.answer4.y = 365
                                                                self.sticky4.rect.x = 655
                                                                self.sticky4.rect.y = 335
                                                                self.answer4_draging = False

                                elif event.type == pygame.MOUSEMOTION:
                                        if self.answer1_draging:
                                                mouse_x, mouse_y = event.pos
                                                self.answer1.x = mouse_x + offset_x + 25
                                                self.answer1.y = mouse_y + offset_y + 30
                                                self.sticky1.rect.x = mouse_x + offset_x
                                                self.sticky1.rect.y = mouse_y + offset_y
                                        elif self.answer2_draging:
                                                mouse_x, mouse_y = event.pos
                                                self.answer2.x = mouse_x + offset_x + 25
                                                self.answer2.y = mouse_y + offset_y + 30
                                                self.sticky2.rect.x = mouse_x + offset_x
                                                self.sticky2.rect.y = mouse_y + offset_y
                                        elif self.answer3_draging:
                                                mouse_x, mouse_y = event.pos
                                                self.answer3.x = mouse_x + offset_x + 25
                                                self.answer3.y = mouse_y + offset_y + 30
                                                self.sticky3.rect.x = mouse_x + offset_x
                                                self.sticky3.rect.y = mouse_y + offset_y
                                        elif self.answer4_draging:
                                                mouse_x, mouse_y = event.pos
                                                self.answer4.x = mouse_x + offset_x + 25
                                                self.answer4.y = mouse_y + offset_y + 30
                                                self.sticky4.rect.x = mouse_x + offset_x
                                                self.sticky4.rect.y = mouse_y + offset_y
                        self.screen.fill(white)
                        self.screen.blit(self.myimage, self.imagerect)
                        self.text(80, 50)

                        answerRect = pygame.Rect(325, 135, 150, 150)
                        pygame.draw.rect(self.screen, pygame.Color("tomato"), answerRect, 5)
                        self.screen.blit(self.sticky1.image, self.sticky1.rect)
                        self.screen.blit(self.sticky2.image, self.sticky2.rect)
                        self.screen.blit(self.sticky3.image, self.sticky3.rect)
                        self.screen.blit(self.sticky4.image, self.sticky4.rect)
                        self.screen.blit(self.label1, self.answer1)
                        self.screen.blit(self.label2, self.answer2)
                        self.screen.blit(self.label3, self.answer3)
                        self.screen.blit(self.label4, self.answer4)
                        self.screen.blit(timer_label, (30, 440))

                        if self.gameover and self.lose_done == 0:
                                self.screen.fill(RED)
                                self.screen.blit(self.gameover_label, (345, 275))
                                pygame.mixer.music.stop()
                                file = 'minigames/armand/assets/lose.ogg'
                                pygame.mixer.init()
                                pygame.mixer.music.load(file)
                                pygame.mixer.music.play()
                                self.lose_done = 1
                                levelComplete = 2
                                break
                        elif self.gameover:
                                self.screen.fill(RED)
                                self.screen.blit(self.gameover_label, (345, 275))
                                levelComplete = 2
                                break

                        if self.correct and self.win_done == 0:
                                self.screen.fill(GREEN)
                                self.screen.blit(self.correct_label, (345, 275))
                                pygame.mixer.music.stop()
                                file = 'minigames/armand/assets/win2.mp3'
                                pygame.mixer.init()
                                pygame.mixer.music.load(file)
                                pygame.mixer.music.play()
                                self.win_done = 1
                                levelComplete = 1
                                break
                        elif self.correct:
                                print("done")
                                self.screen.fill(GREEN)
                                self.screen.blit(self.correct_label, (345, 275))
                                levelComplete = 1
                                break

                        pygame.display.update()







class RunMinigame:
    def main(lvl):
        global levelComplete
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.get_surface()
        game = Main(lvl)
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load('minigames/armand/assets/music.mp3')
        done = False
        pygame.mixer.music.play(loops=-1)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:
                        game = Main(lvl)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                game.levels()
                game.update()
                screen.fill((0, 0, 0))
                pygame.display.flip()
                clock.tick(60)
            if levelComplete == 1:
                print("Player completed the level")
                levelComplete = 0
                return True
            elif levelComplete == 2:
                print("player failed the level")
                levelComplete = 0
                return False
        pygame.key.set_repeat(1, 20)
        pygame.quit()



