from pygame.locals import *
import os, sys, math
import logging
import pygame
from random import randint
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Test Game')
clock = pygame.time.Clock()

wrong = False
gameover = False
correct = False
win_done = 0
lose_done = 0
start_ticks=pygame.time.get_ticks()

myfont = pygame.font.SysFont("comicsansms", 25)
myfont2 = pygame.font.SysFont("comicsansms", 20)

gameover_label = myfont.render("GAMEOVER", 1, (0,0,0))
correct_label = myfont.render("CORRECT", 1, (0,0,0))

myimage = pygame.image.load("assets/bg.png")
stickynote = pygame.image.load("assets/sn.png")
pygame.mixer.init()
pygame.mixer.music.load('assets/music.mp3')

imagerect = myimage.get_rect()

sticky_image = pygame.image.load('assets/sn.png')

file = 'assets/music.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

class Sticky(pygame.sprite.Sprite):

    # Methods
    def __init__(self):

        # Starts the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Sets the stickynote's image
        self.image = sticky_image

        # Sets the stickynote's rect
        self.rect = self.image.get_rect()

        # Set the stickynote's start location
        self.rect.x = 0
        self.rect.y = 0
        
sticky1 = Sticky()
sticky2 = Sticky()
sticky3 = Sticky()
sticky4 = Sticky()

# render text
rect1 = pygame.draw.rect(gameDisplay,white,(80,375,30,30))
rect2 = pygame.draw.rect(gameDisplay,pygame.Color(255, 255, 255, 128),(280,375,30,30))
rect3 = pygame.draw.rect(gameDisplay,white,(480,375,30,30))
rect4 = pygame.draw.rect(gameDisplay,white,(680,375,30,30))
label1 = myfont2.render("Appel", 1, (0,0,0))
label2 = myfont2.render("Kiwi", 1, (0,0,0))
label3 = myfont2.render("Mango", 1, (0,0,0))
label4 = myfont2.render("Peer", 1, (0,0,0))
answer1 = label1.get_rect(center=sticky1.rect.center)
answer2 = label2.get_rect(center=sticky2.rect.center)
answer3 = label3.get_rect(center=sticky3.rect.center)
answer4 = label4.get_rect(center=sticky4.rect.center)
answer1.x = 80
answer1.y = 365
sticky1.rect.x = 55
sticky1.rect.y = 335
answer2.x = 280
answer2.y = 365
sticky2.rect.x = 255
sticky2.rect.y = 335
answer4.x = 680
answer4.y = 365
sticky4.rect.x = 655
sticky4.rect.y = 335
answer3.x = 480
answer3.y = 365
sticky3.rect.x = 455
sticky3.rect.y = 335

level = 5
vraag1 = randint(1, 10)
vraag = vraag1
    
if level == 1 and vraag1 == 1:
        label = myfont.render("Vul aan: De ___ valt niet ver van de boom", 1, (0,0,0))
        label1 = myfont2.render("Appel", 1, (0,0,0))
        label2 = myfont2.render("Kiwi", 1, (0,0,0))
        label3 = myfont2.render("Bes", 1, (0,0,0))
        label4 = myfont2.render("Peer", 1, (0,0,0))
        correct_answer = answer1
elif level == 1 and vraag1 == 2:
        label = myfont.render("Vul aan: Wie de ___ past, trekt hem aan", 1, (0,0,0))
        label1 = myfont2.render("Sok", 1, (0,0,0))
        label2 = myfont2.render("Schoen", 1, (0,0,0))
        label3 = myfont2.render("Laars", 1, (0,0,0))
        label4 = myfont2.render("Hoed", 1, (0,0,0))
        correct_answer = answer2
elif level == 1 and vraag1 == 3:
        label = myfont.render("Vul aan: Iemand een ___ zetten", 1, (0,0,0))
        label1 = myfont2.render("Hak", 1, (0,0,0))
        label2 = myfont2.render("Stap", 1, (0,0,0))
        label3 = myfont2.render("Sprong", 1, (0,0,0))
        label4 = myfont2.render("Thee", 1, (0,0,0))
        correct_answer = answer1
elif level == 1 and vraag1 == 4:
        label = myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0,0,0))
        label1 = myfont2.render("Loon", 1, (0,0,0))
        label2 = myfont2.render("Zoontje", 1, (0,0,0))
        label3 = myfont2.render("Plooitje", 1, (0,0,0))
        label4 = myfont2.render("Boontje", 1, (0,0,0))
        correct_answer = answer4
elif level == 1 and vraag1 == 5:
        label = myfont.render("Vul aan: Zo glad als een ___", 1, (0,0,0))
        label1 = myfont2.render("Koe", 1, (0,0,0))
        label2 = myfont2.render("Meer", 1, (0,0,0))
        label3 = myfont2.render("Aal", 1, (0,0,0))
        label4 = myfont2.render("Aap", 1, (0,0,0))
        correct_answer = answer3
elif level == 1 and vraag1 == 6:
        label = myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0,0,0))
        label1 = myfont2.render("Ja", 1, (0,0,0))
        label2 = myfont2.render("Nee", 1, (0,0,0))
        label3 = myfont2.render("C", 1, (0,0,0))
        label4 = myfont2.render("D", 1, (0,0,0))
        correct_answer = answer4
elif level == 1 and vraag1 == 7:
        label = myfont.render("Vul aan: Niet geschoten is altijd ___", 1, (0,0,0))
        label1 = myfont2.render("Mis", 1, (0,0,0))
        label2 = myfont2.render("Dom", 1, (0,0,0))
        label3 = myfont2.render("Nee", 1, (0,0,0))
        label4 = myfont2.render("Ja", 1, (0,0,0))
        correct_answer = answer1
elif level == 1 and vraag1 == 8:
        label = myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0,0,0))
        label1 = myfont2.render("Een", 1, (0,0,0))
        label2 = myfont2.render("Het", 1, (0,0,0))
        label3 = myfont2.render("Zijn", 1, (0,0,0))
        label4 = myfont2.render("De", 1, (0,0,0))
        correct_answer = answer3
elif level == 1 and vraag1 == 9:
        label = myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Oud", 1, (0,0,0))
        label2 = myfont2.render("Jong", 1, (0,0,0))
        label3 = myfont2.render("Nier", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer2
elif level == 1 and vraag1 == 10:
        label = myfont.render("Vul aan: Jong geleerd, ___ gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Jong", 1, (0,0,0))
        label2 = myfont2.render("Niet", 1, (0,0,0))
        label3 = myfont2.render("Oud", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer3



if level == 2 and vraag1 == 1:
        label = myfont.render("Vul aan: De ___ valt niet ver van de boom", 1, (0,0,0))
        label1 = myfont2.render("Appel", 1, (0,0,0))
        label2 = myfont2.render("Kiwi", 1, (0,0,0))
        label3 = myfont2.render("Bes", 1, (0,0,0))
        label4 = myfont2.render("Peer", 1, (0,0,0))
        correct_answer = answer1
elif level == 2 and vraag1 == 2:
        label = myfont.render("Vul aan: Wie de ___ past, trekt hem aan", 1, (0,0,0))
        label1 = myfont2.render("Sok", 1, (0,0,0))
        label2 = myfont2.render("Schoen", 1, (0,0,0))
        label3 = myfont2.render("Laars", 1, (0,0,0))
        label4 = myfont2.render("Hoed", 1, (0,0,0))
        correct_answer = answer2
elif level == 2 and vraag1 == 3:
        label = myfont.render("Vul aan: Iemand een ___ zetten", 1, (0,0,0))
        label1 = myfont2.render("Hak", 1, (0,0,0))
        label2 = myfont2.render("Stap", 1, (0,0,0))
        label3 = myfont2.render("Sprong", 1, (0,0,0))
        label4 = myfont2.render("Thee", 1, (0,0,0))
        correct_answer = answer1
elif level == 2 and vraag1 == 4:
        label = myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0,0,0))
        label1 = myfont2.render("Loon", 1, (0,0,0))
        label2 = myfont2.render("Zoontje", 1, (0,0,0))
        label3 = myfont2.render("Plooitje", 1, (0,0,0))
        label4 = myfont2.render("Boontje", 1, (0,0,0))
        correct_answer = answer4
elif level == 2 and vraag1 == 5:
        label = myfont.render("Vul aan: Zo glad als een ___", 1, (0,0,0))
        label1 = myfont2.render("Koe", 1, (0,0,0))
        label2 = myfont2.render("Meer", 1, (0,0,0))
        label3 = myfont2.render("Aal", 1, (0,0,0))
        label4 = myfont2.render("Aap", 1, (0,0,0))
        correct_answer = answer3
elif level == 2 and vraag1 == 6:
        label = myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0,0,0))
        label1 = myfont2.render("Ja", 1, (0,0,0))
        label2 = myfont2.render("Nee", 1, (0,0,0))
        label3 = myfont2.render("C", 1, (0,0,0))
        label4 = myfont2.render("D", 1, (0,0,0))
        correct_answer = answer4
elif level == 2 and vraag1 == 7:
        label = myfont.render("Vul aan: Niet geschoten is altijd ___", 1, (0,0,0))
        label1 = myfont2.render("Mis", 1, (0,0,0))
        label2 = myfont2.render("Dom", 1, (0,0,0))
        label3 = myfont2.render("Nee", 1, (0,0,0))
        label4 = myfont2.render("Ja", 1, (0,0,0))
        correct_answer = answer1
elif level == 2 and vraag1 == 8:
        label = myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0,0,0))
        label1 = myfont2.render("Een", 1, (0,0,0))
        label2 = myfont2.render("Het", 1, (0,0,0))
        label3 = myfont2.render("Zijn", 1, (0,0,0))
        label4 = myfont2.render("De", 1, (0,0,0))
        correct_answer = answer3
elif level == 2 and vraag1 == 9:
        label = myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Oud", 1, (0,0,0))
        label2 = myfont2.render("Jong", 1, (0,0,0))
        label3 = myfont2.render("Nier", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer2
elif level == 2 and vraag1 == 10:
        label = myfont.render("Vul aan: Jong geleerd, ___ gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Jong", 1, (0,0,0))
        label2 = myfont2.render("Niet", 1, (0,0,0))
        label3 = myfont2.render("Oud", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer3


if level == 3 and vraag1 == 1:
        label = myfont.render("Vul aan: De ___ valt niet ver van de boom", 1, (0,0,0))
        label1 = myfont2.render("Appel", 1, (0,0,0))
        label2 = myfont2.render("Kiwi", 1, (0,0,0))
        label3 = myfont2.render("Bes", 1, (0,0,0))
        label4 = myfont2.render("Peer", 1, (0,0,0))
        correct_answer = answer1
elif level == 3 and vraag1 == 2:
        label = myfont.render("Vul aan: Wie de ___ past, trekt hem aan", 1, (0,0,0))
        label1 = myfont2.render("Sok", 1, (0,0,0))
        label2 = myfont2.render("Schoen", 1, (0,0,0))
        label3 = myfont2.render("Laars", 1, (0,0,0))
        label4 = myfont2.render("Hoed", 1, (0,0,0))
        correct_answer = answer2
elif level == 3 and vraag1 == 3:
        label = myfont.render("Vul aan: Iemand een ___ zetten", 1, (0,0,0))
        label1 = myfont2.render("Hak", 1, (0,0,0))
        label2 = myfont2.render("Stap", 1, (0,0,0))
        label3 = myfont2.render("Sprong", 1, (0,0,0))
        label4 = myfont2.render("Thee", 1, (0,0,0))
        correct_answer = answer1
elif level == 3 and vraag1 == 4:
        label = myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0,0,0))
        label1 = myfont2.render("Loon", 1, (0,0,0))
        label2 = myfont2.render("Zoontje", 1, (0,0,0))
        label3 = myfont2.render("Plooitje", 1, (0,0,0))
        label4 = myfont2.render("Boontje", 1, (0,0,0))
        correct_answer = answer4
elif level == 3 and vraag1 == 5:
        label = myfont.render("Vul aan: Zo glad als een ___", 1, (0,0,0))
        label1 = myfont2.render("Koe", 1, (0,0,0))
        label2 = myfont2.render("Meer", 1, (0,0,0))
        label3 = myfont2.render("Aal", 1, (0,0,0))
        label4 = myfont2.render("Aap", 1, (0,0,0))
        correct_answer = answer3
elif level == 3 and vraag1 == 6:
        label = myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0,0,0))
        label1 = myfont2.render("Ja", 1, (0,0,0))
        label2 = myfont2.render("Nee", 1, (0,0,0))
        label3 = myfont2.render("C", 1, (0,0,0))
        label4 = myfont2.render("D", 1, (0,0,0))
        correct_answer = answer4
elif level == 3 and vraag1 == 7:
        label = myfont.render("Vul aan: Niet geschoten is altijd ___", 1, (0,0,0))
        label1 = myfont2.render("Mis", 1, (0,0,0))
        label2 = myfont2.render("Dom", 1, (0,0,0))
        label3 = myfont2.render("Nee", 1, (0,0,0))
        label4 = myfont2.render("Ja", 1, (0,0,0))
        correct_answer = answer1
elif level == 3 and vraag1 == 8:
        label = myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0,0,0))
        label1 = myfont2.render("Een", 1, (0,0,0))
        label2 = myfont2.render("Het", 1, (0,0,0))
        label3 = myfont2.render("Zijn", 1, (0,0,0))
        label4 = myfont2.render("De", 1, (0,0,0))
        correct_answer = answer3
elif level == 3 and vraag1 == 9:
        label = myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Oud", 1, (0,0,0))
        label2 = myfont2.render("Jong", 1, (0,0,0))
        label3 = myfont2.render("Nier", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer2
elif level == 3 and vraag1 == 10:
        label = myfont.render("Vul aan: Jong geleerd, ___ gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Jong", 1, (0,0,0))
        label2 = myfont2.render("Niet", 1, (0,0,0))
        label3 = myfont2.render("Oud", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer3



if level == 4 and vraag1 == 1:
        label = myfont.render("Vul aan: De ___ valt niet ver van de boom", 1, (0,0,0))
        label1 = myfont2.render("Appel", 1, (0,0,0))
        label2 = myfont2.render("Kiwi", 1, (0,0,0))
        label3 = myfont2.render("Bes", 1, (0,0,0))
        label4 = myfont2.render("Peer", 1, (0,0,0))
        correct_answer = answer1
elif level == 4 and vraag1 == 2:
        label = myfont.render("Vul aan: Wie de ___ past, trekt hem aan", 1, (0,0,0))
        label1 = myfont2.render("Sok", 1, (0,0,0))
        label2 = myfont2.render("Schoen", 1, (0,0,0))
        label3 = myfont2.render("Laars", 1, (0,0,0))
        label4 = myfont2.render("Hoed", 1, (0,0,0))
        correct_answer = answer2
elif level == 4 and vraag1 == 3:
        label = myfont.render("Vul aan: Iemand een ___ zetten", 1, (0,0,0))
        label1 = myfont2.render("Hak", 1, (0,0,0))
        label2 = myfont2.render("Stap", 1, (0,0,0))
        label3 = myfont2.render("Sprong", 1, (0,0,0))
        label4 = myfont2.render("Thee", 1, (0,0,0))
        correct_answer = answer1
elif level == 4 and vraag1 == 4:
        label = myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0,0,0))
        label1 = myfont2.render("Loon", 1, (0,0,0))
        label2 = myfont2.render("Zoontje", 1, (0,0,0))
        label3 = myfont2.render("Plooitje", 1, (0,0,0))
        label4 = myfont2.render("Boontje", 1, (0,0,0))
        correct_answer = answer4
elif level == 4 and vraag1 == 5:
        label = myfont.render("Vul aan: Zo glad als een ___", 1, (0,0,0))
        label1 = myfont2.render("Koe", 1, (0,0,0))
        label2 = myfont2.render("Meer", 1, (0,0,0))
        label3 = myfont2.render("Aal", 1, (0,0,0))
        label4 = myfont2.render("Aap", 1, (0,0,0))
        correct_answer = answer3
elif level == 4 and vraag1 == 6:
        label = myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0,0,0))
        label1 = myfont2.render("Ja", 1, (0,0,0))
        label2 = myfont2.render("Nee", 1, (0,0,0))
        label3 = myfont2.render("C", 1, (0,0,0))
        label4 = myfont2.render("D", 1, (0,0,0))
        correct_answer = answer4
elif level == 4 and vraag1 == 7:
        label = myfont.render("Vul aan: Niet geschoten is altijd ___", 1, (0,0,0))
        label1 = myfont2.render("Mis", 1, (0,0,0))
        label2 = myfont2.render("Dom", 1, (0,0,0))
        label3 = myfont2.render("Nee", 1, (0,0,0))
        label4 = myfont2.render("Ja", 1, (0,0,0))
        correct_answer = answer1
elif level == 4 and vraag1 == 8:
        label = myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0,0,0))
        label1 = myfont2.render("Een", 1, (0,0,0))
        label2 = myfont2.render("Het", 1, (0,0,0))
        label3 = myfont2.render("Zijn", 1, (0,0,0))
        label4 = myfont2.render("De", 1, (0,0,0))
        correct_answer = answer3
elif level == 4 and vraag1 == 9:
        label = myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Oud", 1, (0,0,0))
        label2 = myfont2.render("Jong", 1, (0,0,0))
        label3 = myfont2.render("Nier", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer2
elif level == 4 and vraag1 == 10:
        label = myfont.render("Vul aan: Jong geleerd, ___ gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Jong", 1, (0,0,0))
        label2 = myfont2.render("Niet", 1, (0,0,0))
        label3 = myfont2.render("Oud", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer3


if level == 5 and vraag1 == 1:
        label = myfont.render("Vul aan: Beter Laat dan ___", 1, (0,0,0))
        label1 = myfont2.render("Nooit", 1, (0,0,0))
        label2 = myfont2.render("Niet", 1, (0,0,0))
        label3 = myfont2.render("Nu", 1, (0,0,0))
        label4 = myfont2.render("Dan", 1, (0,0,0))
        correct_answer = answer1
elif level == 5 and vraag1 == 2:
        label = myfont.render("Vul aan: Nood breekt ___", 1, (0,0,0))
        label1 = myfont2.render("Dat", 1, (0,0,0))
        label2 = myfont2.render("Nood", 1, (0,0,0))
        label3 = myfont2.render("Dit", 1, (0,0,0))
        label4 = myfont2.render("Wet", 1, (0,0,0))
        correct_answer = answer2
elif level == 5 and vraag1 == 3:
        label = myfont.render("Vul aan: ___ breekt wet", 1, (0,0,0))
        label1 = myfont2.render("Nood", 1, (0,0,0))
        label2 = myfont2.render("Dit", 1, (0,0,0))
        label3 = myfont2.render("Hij", 1, (0,0,0))
        label4 = myfont2.render("Dat", 1, (0,0,0))
        correct_answer = answer1
elif level == 5 and vraag1 == 4:
        label = myfont.render("Vul aan: ___ komt om zijn loontje", 1, (0,0,0))
        label1 = myfont2.render("Loon", 1, (0,0,0))
        label2 = myfont2.render("Zoontje", 1, (0,0,0))
        label3 = myfont2.render("Plooitje", 1, (0,0,0))
        label4 = myfont2.render("Boontje", 1, (0,0,0))
        correct_answer = answer4
elif level == 5 and vraag1 == 5:
        label = myfont.render("Vul aan: Zo glad als een ___", 1, (0,0,0))
        label1 = myfont2.render("Koe", 1, (0,0,0))
        label2 = myfont2.render("Meer", 1, (0,0,0))
        label3 = myfont2.render("Aal", 1, (0,0,0))
        label4 = myfont2.render("Aap", 1, (0,0,0))
        correct_answer = answer3
elif level == 5 and vraag1 == 6:
        label = myfont.render("Vul aan: Wie A zegt moet ook ___ zeggen", 1, (0,0,0))
        label1 = myfont2.render("Ja", 1, (0,0,0))
        label2 = myfont2.render("Nee", 1, (0,0,0))
        label3 = myfont2.render("C", 1, (0,0,0))
        label4 = myfont2.render("D", 1, (0,0,0))
        correct_answer = answer4
elif level == 5 and vraag1 == 7:
        label = myfont.render("Vul aan:  Zo lang er ___ is, is er hoop", 1, (0,0,0))
        label1 = myfont2.render("Eten", 1, (0,0,0))
        label2 = myfont2.render("Leven", 1, (0,0,0))
        label3 = myfont2.render("Vrede", 1, (0,0,0))
        label4 = myfont2.render("Dat", 1, (0,0,0))
        correct_answer = answer1
elif level == 5 and vraag1 == 8:
        label = myfont.render("Vul aan: Ieder Huisje heeft ___ kruisje", 1, (0,0,0))
        label1 = myfont2.render("Een", 1, (0,0,0))
        label2 = myfont2.render("Het", 1, (0,0,0))
        label3 = myfont2.render("Zijn", 1, (0,0,0))
        label4 = myfont2.render("De", 1, (0,0,0))
        correct_answer = answer3
elif level == 5 and vraag1 == 9:
        label = myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Oud", 1, (0,0,0))
        label2 = myfont2.render("Jong", 1, (0,0,0))
        label3 = myfont2.render("Nier", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer2
elif level == 5 and vraag1 == 10:
        label = myfont.render("Vul aan: ___ geleerd, oud gedaan.", 1, (0,0,0))
        label1 = myfont2.render("Jong", 1, (0,0,0))
        label2 = myfont2.render("Niet", 1, (0,0,0))
        label3 = myfont2.render("Oud", 1, (0,0,0))
        label4 = myfont2.render("Wel", 1, (0,0,0))
        correct_answer = answer3

        
answer1_draging = False
answer2_draging = False
answer3_draging = False
answer4_draging = False

def text(x,y):
        gameDisplay.blit(label, (x, y))


x = (display_width * 0.15)
y = (display_height * 0.15)



while not wrong:
        
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        second = int(seconds)
        
        if level == 1:
                timer_label = myfont.render("Tijd: " + str(12 - second), 1, (0,0,0))
                if seconds > 12 and correct == False: # if more than 12 seconds close the game
                        gameover = True    
        elif level == 2:
                timer_label = myfont.render("Tijd: " + str(10 - second), 1, (0,0,0))
                if seconds > 10 and correct == False: # if more than 10 seconds close the game
                        gameover = True
        elif level == 3:
                timer_label = myfont.render("Tijd: " + str(8 - second), 1, (0,0,0))
                if seconds > 8 and correct == False: # if more than 8 seconds close the game
                        gameover = True
        elif level == 4:
                timer_label = myfont.render("Tijd: " + str(6 - second), 1, (0,0,0))
                if seconds > 6 and correct == False: # if more than 6 seconds close the game
                        gameover = True
        elif level == 5:

                timer_label = myfont.render("Tijd: " + str(4 - second), 1, (0,0,0))
                if seconds > 4 and correct == False: # if more than 4 seconds close the game
                        gameover = True

       
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        wrong = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if answer1.collidepoint(event.pos):
                            answer1_draging = True
                            test1_dragging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = answer1.x - mouse_x
                            offset_y = answer1.y - mouse_y
                            offset_x = sticky1.rect.x - mouse_x
                            offset_y = sticky1.rect.y - mouse_y
                        elif answer2.collidepoint(event.pos):
                            answer2_draging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = answer2.x - mouse_x
                            offset_y = answer2.y - mouse_y
                            offset_x = sticky2.rect.x - mouse_x
                            offset_y = sticky2.rect.y - mouse_y
                        elif answer3.collidepoint(event.pos):
                            answer3_draging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = answer3.x - mouse_x
                            offset_y = answer3.y - mouse_y
                            offset_x = sticky3.rect.x - mouse_x
                            offset_y = sticky3.rect.y - mouse_y
                        elif answer4.collidepoint(event.pos):
                            answer4_draging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = answer4.x - mouse_x
                            offset_y = answer4.y - mouse_y
                            offset_x = sticky4.rect.x - mouse_x
                            offset_y = sticky4.rect.y - mouse_y
                elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                                if answer1_draging:
                                        if answer1.x >= answerRect.x and answer1.x <= answerRect.x + 75 and answer1.y >= answerRect.y and answer1.y <= answerRect.y + 75:
                                                if correct_answer == answer1:
                                                    answer1_draging = False
                                                    print ('Correct')
                                                    correct = True
                                                else:
                                                    answer1.x = 80
                                                    answer1.y = 365
                                                    sticky1.rect.x = 55
                                                    sticky1.rect.y = 335
                                                    answer1_draging = False
                                                    print ('Wrong')
                                                    gameover = True
                                        else:
                                                answer1.x = 80
                                                answer1.y = 365
                                                sticky1.rect.x = 55
                                                sticky1.rect.y = 335
                                                answer1_draging = False
                                elif answer2_draging:
                                        if answer2.x >= answerRect.x and answer2.x <= answerRect.x + 75 and answer2.y >= answerRect.y and answer2.y <= answerRect.y + 75:
                                                if correct_answer == answer2:
                                                    answer2_draging = False
                                                    print ('Correct')
                                                    correct = True
                                                else:
                                                    answer2.x = 280
                                                    answer2.y = 365
                                                    sticky2.rect.x = 255
                                                    sticky2.rect.y = 335
                                                    answer2_draging = False
                                                    print ('Wrong')
                                                    gameover = True
                                        else:
                                                answer2.x = 280
                                                answer2.y = 365
                                                sticky2.rect.x = 255
                                                sticky2.rect.y = 335
                                                answer2_draging = False
                                elif answer3_draging:
                                        if answer3.x >= answerRect.x and answer3.x <= answerRect.x + 75 and answer3.y >= answerRect.y and answer3.y <= answerRect.y + 75:
                                                if correct_answer == answer3:
                                                    answer3_draging = False
                                                    print ('Correct')
                                                    correct = True
                                                else:
                                                    answer3.x = 480
                                                    answer3.y = 365
                                                    sticky3.rect.x = 455
                                                    sticky3.rect.y = 335
                                                    answer3_draging = False
                                                    print ('Wrong')
                                                    gameover = True
                                        else:
                                                answer3.x = 480
                                                answer3.y = 365
                                                sticky3.rect.x = 455
                                                sticky3.rect.y = 335
                                                answer3_draging = False

                                elif answer4_draging:
                                        if answer4.x >= answerRect.x and answer4.x <= answerRect.x + 75 and answer4.y >= answerRect.y and answer4.y <= answerRect.y + 75:
                                                if correct_answer == answer4:
                                                    answer4_draging = False
                                                    print ('Correct')
                                                    correct = True
                                                else:
                                                    answer4.x = 680
                                                    answer4.y = 365
                                                    sticky4.rect.x = 655
                                                    sticky4.rect.y = 335
                                                    answer4_draging = False
                                                    print ('Wrong')
                                                    gameover = True
                                        else:
                                                answer4.x = 680
                                                answer4.y = 365
                                                sticky4.rect.x = 655
                                                sticky4.rect.y = 335
                                                answer4_draging = False
                                                
                elif event.type == pygame.MOUSEMOTION:
                        if answer1_draging:
                                mouse_x, mouse_y = event.pos
                                answer1.x = mouse_x + offset_x + 25
                                answer1.y = mouse_y + offset_y + 30
                                sticky1.rect.x = mouse_x + offset_x
                                sticky1.rect.y = mouse_y + offset_y
                        elif answer2_draging:
                                mouse_x, mouse_y = event.pos
                                answer2.x = mouse_x + offset_x + 25
                                answer2.y = mouse_y + offset_y + 30
                                sticky2.rect.x = mouse_x + offset_x
                                sticky2.rect.y = mouse_y + offset_y
                        elif answer3_draging:
                                mouse_x, mouse_y = event.pos
                                answer3.x = mouse_x + offset_x + 25
                                answer3.y = mouse_y + offset_y + 30
                                sticky3.rect.x = mouse_x + offset_x
                                sticky3.rect.y = mouse_y + offset_y
                        elif answer4_draging:
                                mouse_x, mouse_y = event.pos
                                answer4.x = mouse_x + offset_x + 25
                                answer4.y = mouse_y + offset_y + 30
                                sticky4.rect.x = mouse_x + offset_x
                                sticky4.rect.y = mouse_y + offset_y
        gameDisplay.fill(white)
        gameDisplay.blit(myimage, imagerect)
        text(80,50)

        answerRect = pygame.Rect(325,135, 150, 150)
        pygame.draw.rect(gameDisplay, pygame.Color("tomato"),answerRect, 5)
        gameDisplay.blit(sticky1.image,sticky1.rect)
        gameDisplay.blit(sticky2.image,sticky2.rect)
        gameDisplay.blit(sticky3.image,sticky3.rect)
        gameDisplay.blit(sticky4.image,sticky4.rect)
        gameDisplay.blit(label1, answer1)
        gameDisplay.blit(label2, answer2)
        gameDisplay.blit(label3, answer3)
        gameDisplay.blit(label4, answer4)
        gameDisplay.blit(timer_label, (30,440))
        

        if gameover == True and lose_done == 0:
            gameDisplay.fill(RED)
            gameDisplay.blit(gameover_label, (345, 275))
            pygame.mixer.music.stop()
            file = 'assets/lose.ogg'
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            lose_done = 1
        elif gameover == True:
            gameDisplay.fill(RED)
            gameDisplay.blit(gameover_label, (345, 275))

        
        if correct == True and win_done == 0:
            gameDisplay.fill(GREEN)
            gameDisplay.blit(correct_label, (345, 275))
            pygame.mixer.music.stop()
            file = 'assets/win2.mp3'
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            win_done = 1
        elif  correct == True:
            gameDisplay.fill(GREEN)
            gameDisplay.blit(correct_label, (345, 275))

        pygame.display.update()
        clock.tick(60)

pygame.quit()
quit()
