import os, sys
import time
import pygame as pg
from pygame.locals import *
sys.path.append('../..')
import MainGame as mg
import Player as player
import LoadAssets as la
from minigames.amar import level1
from minigames.amar import level2
from minigames.amar import level3
from minigames.amar import level4
from minigames.amar import level5
import random
from random import randint, choice

# SCREEN SETTINGS
screen_caption = "School Roamer - Amar"
# Delete this for prod
screen_size = screen_width, screen_height = 800, 600

# ASSETS
bg = pg.image.load("minigames/amar/assets/bg.png")
bg_rect = bg.get_rect()
black = (0, 0, 0)
white =(255, 255, 255)
problem_height = 167.6253

completed = False

def asset(name):
    fullname = os.path.join("assets", name)
    image = pg.image.load(fullname)
    return image, image.get_rect()

class DrawText(object):

    def __init__(self):
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
        self.level = player.level
        self.draw = DrawText()
        self.screen = pg.display.get_surface()
        self.font = pg.font.Font(None, 30)
        self.fsize = 16
        print("Player is level: " + str(self.level))
        self.clock = pg.time.Clock()
        self.timer_lvl1 = 15
        self.timer_lvl2 = 15
        self.timer_lvl3 = 15
        self.timer_lvl4 = 30
        self.timer_lvl5 = 30
        self.timer_reset = 3
        self.dt = 0
        global checkButton
        checkButton = pg.rect.Rect(0, 0, 300, 50)
        checkButton.centerx = 400
        checkButton.centery = 75
        self.problemCompleted = False
        self.problemFailed = False
        self.firstend = True
        self.resetStatus = False
        self.win = pg.mixer.Sound("minigames/amar/assets/win.ogg")
        self.lose = pg.mixer.Sound("minigames/amar/assets/lose.ogg")
        self.ee = pg.mixer.Sound("minigames/amar/assets/ee.ogg")
        self.resetSound = pg.mixer.Sound("minigames/amar/assets/reset.ogg")
        self.reinit()

    def reinit(self):
        print("init")
        if self.level is 1:
            print("Creating level 1 problem")

            global a
            global b
            global c
            global answer
            global numbers
            global posNum
            global choiceNumbers
            global posNumGuess1
            global posNumGuess2
            global sort_answer
            global sort_answer_1
            global sort_answer_2

            global rectangle_1
            global rectangle_1_rect
            global rectangle_1_dragging
            global rectangle_1_number
            global rectangle_2
            global rectangle_2_rect
            global rectangle_2_dragging
            global rectangle_2_number
            global rectangle_3
            global rectangle_3_rect
            global rectangle_3_dragging
            global rectangle_3_number
            global labelRandom

            numbers = []
            choiceNumbers = []
            a, b, c, sort_answer, sort_answer_1, sort_answer_2, answer, extra = level1.gen_problem(self)

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

            rectangle_1 = pg.image.load("minigames/amar/assets/sn.png")
            rectangle_1_rect = rectangle_1.get_rect()
            rectangle_1_rect.x = 137.75
            rectangle_1_rect.y = 300
            rectangle_1_dragging = False
            rectangle_1_number = numbers[posNumGuess1]

            rectangle_2 = pg.image.load("minigames/amar/assets/sn.png")
            rectangle_2_rect = rectangle_2.get_rect()
            rectangle_2_rect.x = 350
            rectangle_2_rect.y = 300
            rectangle_2_dragging = False
            labelRandom = str(extra)

            rectangle_3 = pg.image.load("minigames/amar/assets/sn.png")
            rectangle_3_rect = rectangle_3.get_rect()
            rectangle_3_rect.x = 562.25
            rectangle_3_rect.y = 300
            rectangle_3_dragging = False
            rectangle_3_number = numbers[posNumGuess2]

            answer = str(answer)

            print(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(sort_answer) + ", " + str(answer))
            print("Numbers the user has to put in the right place: " + str(guess1) + " and " + str(guess2))

        elif self.level is 2:
            print("Creating level 2 problem")

            numbers = []
            choiceNumbers = []
            a, b, c, sort_answer, sort_answer_1, sort_answer_2, answer, extra = level2.gen_problem(self)

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

            rectangle_1, rectangle_1_rect = la.asset("sn.png")
            rectangle_1_rect.x = 137.75
            rectangle_1_rect.y = 300
            rectangle_1_dragging = False
            rectangle_1_number = numbers[posNumGuess1]

            rectangle_2, rectangle_2_rect = la.asset("sn.png")
            rectangle_2_rect.x = 350
            rectangle_2_rect.y = 300
            rectangle_2_dragging = False
            rectangle_2_number = numbers[posNumGuess2]

            rectangle_3, rectangle_3_rect = la.asset("sn.png")
            rectangle_3_rect.x = 562.25
            rectangle_3_rect.y = 300
            rectangle_3_dragging = False
            labelRandom = str(extra)

            answer = str(answer)

            print(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(sort_answer) + ", " + str(answer))
            print("Numbers the user has to put in the right place: " + str(guess1) + " and " + str(guess2))

        elif self.level is 3:
            print("Creating level 3 problem")

            numbers = []
            choiceNumbers = []
            a, b, c, sort_answer, sort_answer_1, sort_answer_2, answer, extra = level3.gen_problem(self)

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

            rectangle_1, rectangle_1_rect = la.asset("sn.png")
            rectangle_1_rect.x = 137.75
            rectangle_1_rect.y = 300
            rectangle_1_dragging = False
            labelRandom = str(extra)

            rectangle_2, rectangle_2_rect = la.asset("sn.png")
            rectangle_2_rect.x = 350
            rectangle_2_rect.y = 300
            rectangle_2_dragging = False
            rectangle_2_number = numbers[posNumGuess2]

            rectangle_3, rectangle_3_rect = la.asset("sn.png")
            rectangle_3_rect.x = 562.25
            rectangle_3_rect.y = 300
            rectangle_3_dragging = False
            rectangle_3_number = numbers[posNumGuess1]

            answer = str(answer)

            print(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(sort_answer) + ", " + str(answer))
            print("Numbers the user has to put in the right place: " + str(guess1) + " and " + str(guess2))

        elif self.level is 4:
            print("Creating level 4 problem")

            numbers = []
            choiceNumbers = []
            a, b, c, sort_answer, sort_answer_1, sort_answer_2, answer, extra = level4.gen_problem(self)

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

            rectangle_1, rectangle_1_rect = la.asset("sn.png")
            rectangle_1_rect.x = 117.75
            rectangle_1_rect.y = 300
            rectangle_1_dragging = False
            rectangle_1_number = numbers[posNumGuess1]

            rectangle_2, rectangle_2_rect = la.asset("sn.png")
            rectangle_2_rect.x = 330
            rectangle_2_rect.y = 300
            rectangle_2_dragging = False
            labelRandom = str(extra)

            rectangle_3, rectangle_3_rect = la.asset("sn.png")
            rectangle_3_rect.x = 542.25
            rectangle_3_rect.y = 300
            rectangle_3_dragging = False
            rectangle_3_number = numbers[posNumGuess2]

            answer = str(answer)

            print(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(sort_answer) + ", " + str(answer))
            print("Numbers the user has to put in the right place: " + str(guess1) + " and " + str(guess2))

        elif self.level is 5:
            print("Creating level 5 problem")

            numbers = []
            choiceNumbers = []
            a, b, c, sort_answer, sort_answer_1, sort_answer_2, answer, extra = level5.gen_problem(self)

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

            rectangle_1, rectangle_1_rect = la.asset("sn.png")
            rectangle_1_rect.x = 117.75
            rectangle_1_rect.y = 300
            rectangle_1_dragging = False
            rectangle_1_number = numbers[posNumGuess1]

            rectangle_2, rectangle_2_rect = la.asset("sn.png")
            rectangle_2_rect.x = 330
            rectangle_2_rect.y = 300
            rectangle_2_dragging = False
            rectangle_2_number = numbers[posNumGuess2]

            rectangle_3, rectangle_3_rect = la.asset("sn.png")
            rectangle_3_rect.x = 542.25
            rectangle_3_rect.y = 300
            rectangle_3_dragging = False
            labelRandom = str(extra)

            answer = str(answer)

            print(str(a) + ", " + str(b) + ", " + str(c) + ", " + str(sort_answer) + ", " + str(answer))
            print("Numbers the user has to put in the right place: " + str(guess1) + " and " + str(guess2))

    def reset(self):
        print("resetting")
        if self.level is 1 or 2 or 3:
            print("Wrong!")
            self.resetSound.play(loops=0)
            self.resetStatus = True
            rectangle_1_rect.x = 137.75
            rectangle_1_rect.y = 300

            rectangle_2_rect.x = 350
            rectangle_2_rect.y = 300

            rectangle_3_rect.x = 562.25
            rectangle_3_rect.y = 300
        elif self.level is 4 or 5:
            print("Wrong!")
            self.resetSound.play(loops=0)
            self.resetStatus = True
            rectangle_1_rect.x = 117.75
            rectangle_1_rect.y = 300

            rectangle_2_rect.x = 330
            rectangle_2_rect.y = 300

            rectangle_3_rect.x = 542.25
            rectangle_3_rect.y = 300

    def check(self):
        print("------------------")
        print("Checking answer...")

        if self.level is 1:
            print("Level 1 problem")

            global posNum
            global sort_answer

            a = 0
            b = 0
            c = 0

            print("Rectangle 1: " + str(rectangle_1_rect))
            print("Rectangle 1 pos1: " + str(rectangle_1_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 1 pos2: " + str(rectangle_1_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 1 pos3: " + str(rectangle_1_rect.collidepoint(563.5, problem_height)))
            print("Rectangle 2: " + str(rectangle_3_rect))
            print("Rectangle 2 pos1: " + str(rectangle_3_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 2 pos2: " + str(rectangle_3_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 2 pos3: " + str(rectangle_3_rect.collidepoint(563.5, problem_height)))

            if rectangle_1_rect.collidepoint(187.5, problem_height):
                print("Rectangle 1 is in pos 1")
                a = rectangle_1_number
                print("a is: " + str(a))
                if rectangle_3_rect.collidepoint(375.5, problem_height) and posNum is 2:
                    print("Rectangle 2 is in pos 2")
                    b = rectangle_3_number
                    print("b is: " + str(b))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_3_rect.collidepoint(563.5, problem_height) and posNum is 1:
                    print("Rectangle 2 is in pos 3")
                    c = rectangle_3_number
                    print("c is: " + str(c))
                    b = numbers[posNum]
                    print("b is: " + str(b))
            elif rectangle_1_rect.collidepoint(375.5, problem_height):
                print("Rectangle 1 is in pos 2")
                b = rectangle_1_number
                print("b is: " + str(b))
                if rectangle_3_rect.collidepoint(187.5, problem_height) and posNum is 2:
                    print("Rectangle 2 is in pos 1")
                    a = rectangle_3_number
                    print("a is: " + str(a))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_3_rect.collidepoint(563.5, problem_height) and posNum is 0:
                    print("Rectangle 2 is in pos 3")
                    c = rectangle_3_number
                    print("c is: " + str(c))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            elif rectangle_1_rect.collidepoint(563.5, problem_height):
                print("Rectangle 1 is in pos 3")
                c = rectangle_1_number
                print("c is: " + str(c))
                if rectangle_3_rect.collidepoint(187.5, problem_height) and posNum is 1:
                    print("Rectangle 2 is in pos 1")
                    a = rectangle_3_number
                    print("a is: " + str(a))
                    b = numbers[posNum]
                    print("b is: " + str(b))
                    print("Rectangle 2 wasn't set!")
                elif rectangle_3_rect.collidepoint(375.5, problem_height) and posNum is 0:
                    print("Rectangle 2 is in pos 2")
                    b = rectangle_3_number
                    print("b is: " + str(b))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            else:
                print("rect1 was not set")

            if sort_answer == "a + b + c":
                print("Sort answer is " + str(sort_answer))
                a = a + b
                a = a + c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    self.reset()
            elif sort_answer == "a - b + c":
                print("Sort answer is " + str(sort_answer))
                a = a - b
                a = a + c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    self.reset()
            elif sort_answer == "a + b - c":
                print("Sort answer is " + str(sort_answer))
                a = a + b
                a = a - c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    self.reset()
            elif sort_answer == "a - b - c":
                print("Sort answer is " + str(sort_answer))
                a = a - b
                a = a - c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    self.reset()

        elif self.level is 2:
            print("Level 2 problem")

            a = 0
            b = 0
            c = 0

            print("Rectangle 1: " + str(rectangle_1_rect))
            print("Rectangle 1 pos1: " + str(rectangle_1_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 1 pos2: " + str(rectangle_1_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 1 pos3: " + str(rectangle_1_rect.collidepoint(563.5, problem_height)))
            print("Rectangle 2: " + str(rectangle_2_rect))
            print("Rectangle 2 pos1: " + str(rectangle_2_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 2 pos2: " + str(rectangle_2_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 2 pos3: " + str(rectangle_2_rect.collidepoint(563.5, problem_height)))

            if rectangle_1_rect.collidepoint(187.5, problem_height):
                print("Rectangle 1 is in pos 1")
                a = rectangle_1_number
                print("a is: " + str(a))
                if rectangle_2_rect.collidepoint(375.5, problem_height) and posNum is 2:
                    print("Rectangle 2 is in pos 2")
                    b = rectangle_2_number
                    print("b is: " + str(b))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_2_rect.collidepoint(563.5, problem_height) and posNum is 1:
                    print("Rectangle 2 is in pos 3")
                    c = rectangle_2_number
                    print("c is: " + str(c))
                    b = numbers[posNum]
                    print("b is: " + str(b))
            elif rectangle_1_rect.collidepoint(375.5, problem_height):
                print("Rectangle 1 is in pos 2")
                b = rectangle_1_number
                print("b is: " + str(b))
                if rectangle_2_rect.collidepoint(187.5, problem_height) and posNum is 2:
                    print("Rectangle 2 is in pos 1")
                    a = rectangle_2_number
                    print("a is: " + str(a))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_2_rect.collidepoint(563.5, problem_height) and posNum is 0:
                    print("Rectangle 2 is in pos 3")
                    c = rectangle_2_number
                    print("c is: " + str(c))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            elif rectangle_1_rect.collidepoint(563.5, problem_height):
                print("Rectangle 1 is in pos 3")
                c = rectangle_1_number
                print("c is: " + str(c))
                if rectangle_2_rect.collidepoint(187.5, problem_height) and posNum is 1:
                    print("Rectangle 2 is in pos 1")
                    a = rectangle_2_number
                    print("a is: " + str(a))
                    b = numbers[posNum]
                    print("b is: " + str(b))
                    print("Rectangle 2 wasn't set!")
                elif rectangle_2_rect.collidepoint(375.5, problem_height) and posNum is 0:
                    print("Rectangle 2 is in pos 2")
                    b = rectangle_2_number
                    print("b is: " + str(b))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            else:
                print("rect1 was not set")

            if sort_answer == "a + b + c":
                print("Sort answer is " + str(sort_answer))
                a = a + b
                a = a + c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    print("Wrong!")
                    self.reset()
                    rectangle_1_rect.x = 137.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 350
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 562.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a - b + c":
                print("Sort answer is " + str(sort_answer))
                a = a - b
                a = a + c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    print("Wrong!")
                    self.reset()
                    rectangle_1_rect.x = 137.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 350
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 562.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a + b - c":
                print("Sort answer is " + str(sort_answer))
                a = a + b
                a = a - c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    print("Wrong!")
                    self.reset()
                    rectangle_1_rect.x = 137.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 350
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 562.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a - b - c":
                print("Sort answer is " + str(sort_answer))
                a = a - b
                a = a - c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    print("Wrong!")
                    self.reset()
                    rectangle_1_rect.x = 137.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 350
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 562.25
                    rectangle_3_rect.y = 300

        elif self.level is 3:
            print("Level 3 problem")

            a = 0
            b = 0
            c = 0

            print("Rectangle 2: " + str(rectangle_2_rect))
            print("Rectangle 2 pos1: " + str(rectangle_2_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 2 pos2: " + str(rectangle_2_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 2 pos3: " + str(rectangle_2_rect.collidepoint(563.5, problem_height)))
            print("Rectangle 3: " + str(rectangle_3_rect))
            print("Rectangle 3 pos1: " + str(rectangle_3_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 3 pos2: " + str(rectangle_3_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 3 pos3: " + str(rectangle_3_rect.collidepoint(563.5, problem_height)))

            if rectangle_2_rect.collidepoint(187.5, problem_height):
                print("Rectangle 2 is in pos 1")
                a = rectangle_2_number
                print("a is: " + str(a))
                if rectangle_3_rect.collidepoint(375.5, problem_height) and posNum is 2:
                    print("Rectangle 3 is in pos 3")
                    b = rectangle_3_number
                    print("b is: " + str(b))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_3_rect.collidepoint(563.5, problem_height) and posNum is 1:
                    print("Rectangle 3 is in pos 3")
                    c = rectangle_3_number
                    print("c is: " + str(c))
                    b = numbers[posNum]
                    print("b is: " + str(b))
            elif rectangle_2_rect.collidepoint(375.5, problem_height):
                print("Rectangle 2 is in pos 3")
                b = rectangle_2_number
                print("b is: " + str(b))
                if rectangle_3_rect.collidepoint(187.5, problem_height) and posNum is 2:
                    print("Rectangle 3 is in pos 3")
                    a = rectangle_3_number
                    print("a is: " + str(a))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_3_rect.collidepoint(563.5, problem_height) and posNum is 0:
                    print("Rectangle 3 is in pos 3")
                    c = rectangle_3_number
                    print("c is: " + str(c))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            elif rectangle_2_rect.collidepoint(563.5, problem_height):
                print("Rectangle 2 is in pos 3")
                c = rectangle_2_number
                print("c is: " + str(c))
                if rectangle_3_rect.collidepoint(187.5, problem_height) and posNum is 1:
                    print("Rectangle 3 is in pos 3")
                    a = rectangle_3_number
                    print("a is: " + str(a))
                    b = numbers[posNum]
                    print("b is: " + str(b))
                    print("Rectangle 3 wasn't set!")
                elif rectangle_3_rect.collidepoint(375.5, problem_height) and posNum is 0:
                    print("Rectangle 3 is in pos 3")
                    b = rectangle_3_number
                    print("b is: " + str(b))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            else:
                print("rect2 was not set")

            if sort_answer == "a + b + c":
                print("Sort answer is " + str(sort_answer))
                a = a + b
                a = a + c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    print("Wrong!")
                    self.reset()
                    rectangle_1_rect.x = 137.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 350
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 562.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a - b + c":
                print("Sort answer is " + str(sort_answer))
                a = a - b
                a = a + c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    print("Wrong!")
                    self.reset()
                    rectangle_1_rect.x = 137.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 350
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 562.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a + b - c":
                print("Sort answer is " + str(sort_answer))
                a = a + b
                a = a - c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    print("Wrong!")
                    self.reset()
                    rectangle_1_rect.x = 137.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 350
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 562.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a - b - c":
                print("Sort answer is " + str(sort_answer))
                a = a - b
                a = a - c
                a = str(a)
                print(str(a))
                if a == answer:
                    print("Correct!")
                    self.problemCompleted = True
                else:
                    print("Wrong!")
                    self.reset()
                    rectangle_1_rect.x = 137.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 350
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 562.25
                    rectangle_3_rect.y = 300

        elif self.level is 4:
            print("Level 4 problem")

            a = 0
            b = 0
            c = 0

            print("Rectangle 1: " + str(rectangle_1_rect))
            print("Rectangle 1 pos1: " + str(rectangle_1_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 1 pos2: " + str(rectangle_1_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 1 pos3: " + str(rectangle_1_rect.collidepoint(563.5, problem_height)))
            print("Rectangle 3: " + str(rectangle_3_rect))
            print("Rectangle 3 pos1: " + str(rectangle_3_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 3 pos2: " + str(rectangle_3_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 3 pos3: " + str(rectangle_3_rect.collidepoint(563.5, problem_height)))

            if rectangle_1_rect.collidepoint(187.5, problem_height):
                print("Rectangle 1 is in pos 1")
                a = rectangle_1_number
                print("a is: " + str(a))
                if rectangle_3_rect.collidepoint(375.5, problem_height) and posNum is 2:
                    print("Rectangle 3 is in pos 3")
                    b = rectangle_3_number
                    print("b is: " + str(b))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_3_rect.collidepoint(563.5, problem_height) and posNum is 1:
                    print("Rectangle 3 is in pos 3")
                    c = rectangle_3_number
                    print("c is: " + str(c))
                    b = numbers[posNum]
                    print("b is: " + str(b))
            elif rectangle_1_rect.collidepoint(375.5, problem_height):
                print("Rectangle 1 is in pos 1")
                b = rectangle_1_number
                print("b is: " + str(b))
                if rectangle_3_rect.collidepoint(187.5, problem_height) and posNum is 2:
                    print("Rectangle 3 is in pos 3")
                    a = rectangle_3_number
                    print("a is: " + str(a))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_3_rect.collidepoint(563.5, problem_height) and posNum is 0:
                    print("Rectangle 3 is in pos 3")
                    c = rectangle_3_number
                    print("c is: " + str(c))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            elif rectangle_1_rect.collidepoint(563.5, problem_height):
                print("Rectangle 1 is in pos 1")
                c = rectangle_1_number
                print("c is: " + str(c))
                if rectangle_3_rect.collidepoint(187.5, problem_height) and posNum is 1:
                    print("Rectangle 3 is in pos 3")
                    a = rectangle_3_number
                    print("a is: " + str(a))
                    b = numbers[posNum]
                    print("b is: " + str(b))
                    print("Rectangle 3 wasn't set!")
                elif rectangle_3_rect.collidepoint(375.5, problem_height) and posNum is 0:
                    print("Rectangle 3 is in pos 3")
                    b = rectangle_3_number
                    print("b is: " + str(b))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            else:
                print("rect2 was not set")

            if sort_answer == "a x b + c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    a = a * b
                    a = a + c
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a x b - c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    a = a * b
                    a = a - c
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a - b x c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    b = b * c
                    a = a - b
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a + b x c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    b = b * c
                    a = a + b
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a / b + c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    a = a / b
                    a = a + c
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a / b - c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    a = a / b
                    a = a - c
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a + b / c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    b = b / c
                    a = a + b
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a - b / c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    b = b / c
                    a = a - b
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300

        elif self.level is 5:
            print("Level 5 problem")

            a = 0
            b = 0
            c = 0

            print("Rectangle 1: " + str(rectangle_1_rect))
            print("Rectangle 1 pos1: " + str(rectangle_1_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 1 pos2: " + str(rectangle_1_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 1 pos3: " + str(rectangle_1_rect.collidepoint(563.5, problem_height)))
            print("Rectangle 2: " + str(rectangle_2_rect))
            print("Rectangle 2 pos1: " + str(rectangle_2_rect.collidepoint(187.5, problem_height)))
            print("Rectangle 2 pos2: " + str(rectangle_2_rect.collidepoint(375.5, problem_height)))
            print("Rectangle 2 pos3: " + str(rectangle_2_rect.collidepoint(563.5, problem_height)))

            if rectangle_1_rect.collidepoint(187.5, problem_height):
                print("Rectangle 1 is in pos 1")
                a = rectangle_1_number
                print("a is: " + str(a))
                if rectangle_2_rect.collidepoint(375.5, problem_height) and posNum is 2:
                    print("Rectangle 3 is in pos 3")
                    b = rectangle_2_number
                    print("b is: " + str(b))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_2_rect.collidepoint(563.5, problem_height) and posNum is 1:
                    print("Rectangle 3 is in pos 3")
                    c = rectangle_2_number
                    print("c is: " + str(c))
                    b = numbers[posNum]
                    print("b is: " + str(b))
            elif rectangle_1_rect.collidepoint(375.5, problem_height):
                print("Rectangle 1 is in pos 1")
                b = rectangle_1_number
                print("b is: " + str(b))
                if rectangle_2_rect.collidepoint(187.5, problem_height) and posNum is 2:
                    print("Rectangle 3 is in pos 3")
                    a = rectangle_2_number
                    print("a is: " + str(a))
                    c = numbers[posNum]
                    print("c is: " + str(c))
                elif rectangle_2_rect.collidepoint(563.5, problem_height) and posNum is 0:
                    print("Rectangle 3 is in pos 3")
                    c = rectangle_2_number
                    print("c is: " + str(c))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            elif rectangle_1_rect.collidepoint(563.5, problem_height):
                print("Rectangle 1 is in pos 1")
                c = rectangle_1_number
                print("c is: " + str(c))
                if rectangle_2_rect.collidepoint(187.5, problem_height) and posNum is 1:
                    print("Rectangle 3 is in pos 3")
                    a = rectangle_2_number
                    print("a is: " + str(a))
                    b = numbers[posNum]
                    print("b is: " + str(b))
                    print("Rectangle 3 wasn't set!")
                elif rectangle_2_rect.collidepoint(375.5, problem_height) and posNum is 0:
                    print("Rectangle 3 is in pos 3")
                    b = rectangle_2_number
                    print("b is: " + str(b))
                    a = numbers[posNum]
                    print("a is: " + str(a))
            else:
                print("rect2 was not set")

            if sort_answer == "a x b + c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    a = a * b
                    a = a + c
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a x b - c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    a = a * b
                    a = a - c
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a - b x c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    b = b * c
                    a = a - b
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a + b x c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    b = b * c
                    a = a + b
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a / b + c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    a = a / b
                    a = a + c
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a / b - c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    a = a / b
                    a = a - c
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a + b / c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    b = b / c
                    a = a + b
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300
            elif sort_answer == "a - b / c":
                if a or b or c is not 0:
                    print("Sort answer is " + str(sort_answer))
                    b = b / c
                    a = a - b
                    a = round(a, 1)
                    a = str(a)
                    print(str(a))
                    if a == answer:
                        print("Correct!")
                        self.problemCompleted = True
                    else:
                        print("Wrong!")
                        self.reset()
                        rectangle_1_rect.x = 117.75
                        rectangle_1_rect.y = 300

                        rectangle_2_rect.x = 330
                        rectangle_2_rect.y = 300

                        rectangle_3_rect.x = 542.25
                        rectangle_3_rect.y = 300
                else:
                    print("Not all sticky notes were placed, try again")
                    self.reset()
                    rectangle_1_rect.x = 117.75
                    rectangle_1_rect.y = 300

                    rectangle_2_rect.x = 330
                    rectangle_2_rect.y = 300

                    rectangle_3_rect.x = 542.25
                    rectangle_3_rect.y = 300

    def control(self):

        global checkButton
        global rectangle_1_dragging
        rectangle_1_dragging = rectangle_1_dragging
        global rectangle_2_dragging
        rectangle_2_dragging = rectangle_2_dragging
        global rectangle_3_dragging
        rectangle_3_dragging = rectangle_3_dragging
        offset_x = -50
        offset_y = -50

        for event in pg.event.get():

            # QUIT
            if event.type == QUIT:
                print("ESCAPE")
                Minigame.state = False

            # MOUSE UP
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    rectangle_1_dragging = False
                    rectangle_2_dragging = False
                    rectangle_3_dragging = False

            # MOUSE DOWN
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rectangle_1_rect.collidepoint(event.pos):
                        rectangle_1_dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle_1_rect.x - mouse_x
                        offset_y = rectangle_1_rect.y - mouse_y
                    if rectangle_2_rect.collidepoint(event.pos):
                        rectangle_2_dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle_2_rect.x - mouse_x
                        offset_y = rectangle_2_rect.y - mouse_y
                    if rectangle_3_rect.collidepoint(event.pos):
                        rectangle_3_dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle_3_rect.x - mouse_x
                        offset_y = rectangle_3_rect.y - mouse_y
                    if checkButton.collidepoint(event.pos):
                        self.check()

            elif event.type == pg.MOUSEMOTION:
                if rectangle_1_dragging:
                    mouse_x, mouse_y = event.pos
                    rectangle_1_rect.x = mouse_x + offset_x
                    rectangle_1_rect.y = mouse_y + offset_y
                if rectangle_2_dragging:
                    mouse_x, mouse_y = event.pos
                    rectangle_2_rect.x = mouse_x + offset_x
                    rectangle_2_rect.y = mouse_y + offset_y
                if rectangle_3_dragging:
                    mouse_x, mouse_y = event.pos
                    rectangle_3_rect.x = mouse_x + offset_x
                    rectangle_3_rect.y = mouse_y + offset_y

            # KEYDOWN
            elif event.type == KEYDOWN:
                # Check for escape key, when pressed, quit the game
                if event.key == K_ESCAPE:
                    print("ESCAPE MINIGAME")
                    Minigame.state = False
                if event.key == K_h:
                    self.ee.play(loops=0)

    def render(self):

        if self.firstend:
            self.screen.blit(bg, (0,0))
            self.draw.rt(self.screen, "Level: " + str(self.level), 30, None, black, 695, 30, 1)

            if self.level is 1 and self.firstend:
                if posNum is 0:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 187.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 375.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 563.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 563.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 375.5, problem_height, 1)
                elif posNum is 1:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 375.5, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 187.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 563.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 563.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 187.5, problem_height, 1)
                elif posNum is 2:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 563.25, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 187.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 375.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 375.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 187.5, problem_height, 1)
                self.draw.rt(self.screen, sort_answer_1, 70, None, black, 281.25, problem_height, 1)
                self.draw.rt(self.screen, str(sort_answer_2), 70, None, black, 469.375, problem_height, 1)
                self.draw.rt(self.screen, "= " + str(answer), 70, None, black, 650, problem_height, 1)

                # Sticky Note 1
                self.screen.blit(rectangle_1, rectangle_1_rect)

                self.font = pg.font.Font(None, 70)
                label1 = str(numbers[posNumGuess1])
                label1 = self.font.render(label1, 1, (0, 0, 0))
                self.screen.blit(label1, ((rectangle_1_rect.centerx - (label1.get_rect().width / 2)), (rectangle_1_rect.centery - (label1.get_rect().height / 2))))

                # Sticky Note 2
                self.screen.blit(rectangle_3, rectangle_3_rect)

                self.font = pg.font.Font(None, 70)
                label2 = str(numbers[posNumGuess2])
                label2 = self.font.render(label2, 1, (0, 0, 0))
                self.screen.blit(label2, ((rectangle_3_rect.centerx - (label2.get_rect().width / 2)), (rectangle_3_rect.centery - (label2.get_rect().height / 2))))

                # Sticky Note 3
                self.screen.blit(rectangle_2, rectangle_2_rect)

                self.font = pg.font.Font(None, 70)
                self.labelRandom = self.font.render(labelRandom, 1, (0, 0, 0))
                self.screen.blit(self.labelRandom, ((rectangle_2_rect.centerx - (self.labelRandom.get_rect().width / 2)), (rectangle_2_rect.centery - (self.labelRandom.get_rect().height / 2))))

                # Timer level 1
                self.timer_lvl1 -= self.dt

                self.font = pg.font.Font(None, 30)
                txt = self.font.render("Timer: " + str(round(self.timer_lvl1, 0)), True, black)
                self.screen.blit(txt, (30, 30))

                if self.timer_lvl1 <= 0:
                    self.problemFailed = True

            elif self.level is 2 and self.firstend:
                if posNum is 0:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 187.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 375.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 563.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 563.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 375.5, problem_height, 1)
                elif posNum is 1:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 375.5, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 187.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 563.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 563.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 187.5, problem_height, 1)
                elif posNum is 2:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 563.25, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 187.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 375.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 375.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 187.5, problem_height, 1)
                self.draw.rt(self.screen, sort_answer_1, 70, None, black, 281.25, problem_height, 1)
                self.draw.rt(self.screen, str(sort_answer_2), 70, None, black, 469.375, problem_height, 1)
                self.draw.rt(self.screen, "= " + str(answer), 70, None, black, 650, problem_height, 1)

                # Sticky Note 1
                self.screen.blit(rectangle_1, rectangle_1_rect)

                self.font = pg.font.Font(None, 70)
                label1 = str(numbers[posNumGuess1])
                label1 = self.font.render(label1, 1, (0, 0, 0))
                self.screen.blit(label1, ((rectangle_1_rect.centerx - (label1.get_rect().width / 2)), (rectangle_1_rect.centery - (label1.get_rect().height / 2))))

                # Sticky Note 2
                self.screen.blit(rectangle_2, rectangle_2_rect)

                self.font = pg.font.Font(None, 70)
                label2 = str(numbers[posNumGuess2])
                label2 = self.font.render(label2, 1, (0, 0, 0))
                self.screen.blit(label2, ((rectangle_2_rect.centerx - (label2.get_rect().width / 2)), (rectangle_2_rect.centery - (label2.get_rect().height / 2))))

                # Sticky Note 3
                self.screen.blit(rectangle_3, rectangle_3_rect)

                self.font = pg.font.Font(None, 70)
                self.labelRandom = self.font.render(labelRandom, 1, (0, 0, 0))
                self.screen.blit(self.labelRandom, ((rectangle_3_rect.centerx - (self.labelRandom.get_rect().width / 2)), (rectangle_3_rect.centery - (self.labelRandom.get_rect().height / 2))))

                # Timer level 2
                self.timer_lvl2 -= self.dt

                self.font = pg.font.Font(None, 30)
                txt = self.font.render("Timer: " + str(round(self.timer_lvl2, 0)), True, black)
                self.screen.blit(txt, (30, 30))

                if self.timer_lvl2 <= 0:
                    self.problemFailed = True

            elif self.level is 3 and self.firstend:
                if posNum is 0:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 187.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 375.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 563.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 563.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 375.5, problem_height, 1)
                elif posNum is 1:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 375.5, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 187.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 563.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 563.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 187.5, problem_height, 1)
                elif posNum is 2:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 563.25, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 187.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 375.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 375.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 187.5, problem_height, 1)
                self.draw.rt(self.screen, sort_answer_1, 70, None, black, 281.25, problem_height, 1)
                self.draw.rt(self.screen, str(sort_answer_2), 70, None, black, 469.375, problem_height, 1)
                self.draw.rt(self.screen, "= " + str(answer), 70, None, black, 650, problem_height, 1)

                # Sticky Note 2
                self.screen.blit(rectangle_2, rectangle_2_rect)

                self.font = pg.font.Font(None, 70)
                label1 = str(numbers[posNumGuess1])
                label1 = self.font.render(label1, 1, (0, 0, 0))
                self.screen.blit(label1, ((rectangle_2_rect.centerx - (label1.get_rect().width / 2)), (rectangle_2_rect.centery - (label1.get_rect().height / 2))))

                # Sticky Note 3
                self.screen.blit(rectangle_3, rectangle_3_rect)

                self.font = pg.font.Font(None, 70)
                label2 = str(numbers[posNumGuess2])
                label2 = self.font.render(label2, 1, (0, 0, 0))
                self.screen.blit(label2, ((rectangle_3_rect.centerx - (label2.get_rect().width / 2)), (rectangle_3_rect.centery - (label2.get_rect().height / 2))))

                # Sticky Note 1
                self.screen.blit(rectangle_1, rectangle_1_rect)

                self.font = pg.font.Font(None, 70)
                self.labelRandom = self.font.render(labelRandom, 1, (0, 0, 0))
                self.screen.blit(self.labelRandom, ((rectangle_1_rect.centerx - (self.labelRandom.get_rect().width / 2)), (rectangle_1_rect.centery - (self.labelRandom.get_rect().height / 2))))

                # Timer level 3
                self.timer_lvl3 -= self.dt

                self.font = pg.font.Font(None, 30)
                txt = self.font.render("Timer: " + str(round(self.timer_lvl3, 0)), True, black)
                self.screen.blit(txt, (30, 30))

                if self.timer_lvl3 <= 0:
                    self.problemFailed = True

            elif self.level is 4 and self.firstend:
                if posNum is 0:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 167.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 355.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 543.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 543.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 355.5, problem_height, 1)
                elif posNum is 1:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 355.5, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 167.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 543.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 543.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 167.5, problem_height, 1)
                elif posNum is 2:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 543.25, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 167.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 355.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 355.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 167.5, problem_height, 1)
                self.draw.rt(self.screen, sort_answer_1, 70, None, black, 261.25, problem_height, 1)
                self.draw.rt(self.screen, str(sort_answer_2), 70, None, black, 449.375, problem_height, 1)
                self.draw.rt(self.screen, "= " + str(answer), 70, None, black, 630, problem_height, 1)

                # Sticky Note 2
                self.screen.blit(rectangle_1, rectangle_1_rect)

                self.font = pg.font.Font(None, 70)
                label1 = str(numbers[posNumGuess1])
                label1 = self.font.render(label1, 1, (0, 0, 0))
                self.screen.blit(label1, ((rectangle_1_rect.centerx - (label1.get_rect().width / 2)), (rectangle_1_rect.centery - (label1.get_rect().height / 2))))

                # Sticky Note 3
                self.screen.blit(rectangle_3, rectangle_3_rect)

                self.font = pg.font.Font(None, 70)
                label2 = str(numbers[posNumGuess2])
                label2 = self.font.render(label2, 1, (0, 0, 0))
                self.screen.blit(label2, ((rectangle_3_rect.centerx - (label2.get_rect().width / 2)), (rectangle_3_rect.centery - (label2.get_rect().height / 2))))

                # Sticky Note 1
                self.screen.blit(rectangle_2, rectangle_2_rect)

                self.font = pg.font.Font(None, 70)
                self.labelRandom = self.font.render(labelRandom, 1, (0, 0, 0))
                self.screen.blit(self.labelRandom, ((rectangle_2_rect.centerx - (self.labelRandom.get_rect().width / 2)), (rectangle_2_rect.centery - (self.labelRandom.get_rect().height / 2))))

                # Timer level 3
                self.timer_lvl4 -= self.dt

                self.font = pg.font.Font(None, 30)
                txt = self.font.render("Timer: " + str(round(self.timer_lvl4, 0)), True, black)
                self.screen.blit(txt, (30, 30))

                if self.timer_lvl4 <= 0:
                    self.problemFailed = True

            elif self.level is 5 and self.firstend:
                if posNum is 0:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 167.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 355.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 543.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 543.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 355.5, problem_height, 1)
                elif posNum is 1:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 355.5, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 167.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 543.25, problem_height, 1)
                    if posNumGuess1 is 2:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 543.25, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 167.5, problem_height, 1)
                elif posNum is 2:
                    self.draw.rt(self.screen, numbers[posNum], 70, None, black, 543.25, problem_height, 1)
                    if posNumGuess1 is 0:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 167.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 355.5, problem_height, 1)
                    if posNumGuess1 is 1:
                        self.draw.rt(self.screen, numbers[posNumGuess1], 70, None, white, 355.5, problem_height, 1)
                        self.draw.rt(self.screen, numbers[posNumGuess2], 70, None, white, 167.5, problem_height, 1)
                self.draw.rt(self.screen, sort_answer_1, 70, None, black, 261.25, problem_height, 1)
                self.draw.rt(self.screen, str(sort_answer_2), 70, None, black, 449.375, problem_height, 1)
                self.draw.rt(self.screen, "= " + str(answer), 70, None, black, 610, problem_height, 1)

                # Sticky Note 2
                self.screen.blit(rectangle_1, rectangle_1_rect)

                self.font = pg.font.Font(None, 70)
                label1 = str(numbers[posNumGuess1])
                label1 = self.font.render(label1, 1, (0, 0, 0))
                self.screen.blit(label1, ((rectangle_1_rect.centerx - (label1.get_rect().width / 2)), (rectangle_1_rect.centery - (label1.get_rect().height / 2))))

                # Sticky Note 3
                self.screen.blit(rectangle_2, rectangle_2_rect)

                self.font = pg.font.Font(None, 70)
                label2 = str(numbers[posNumGuess2])
                label2 = self.font.render(label2, 1, (0, 0, 0))
                self.screen.blit(label2, ((rectangle_2_rect.centerx - (label2.get_rect().width / 2)), (rectangle_2_rect.centery - (label2.get_rect().height / 2))))

                # Sticky Note 1
                self.screen.blit(rectangle_3, rectangle_3_rect)

                self.font = pg.font.Font(None, 70)
                self.labelRandom = self.font.render(labelRandom, 1, (0, 0, 0))
                self.screen.blit(self.labelRandom, ((rectangle_3_rect.centerx - (self.labelRandom.get_rect().width / 2)), (rectangle_3_rect.centery - (self.labelRandom.get_rect().height / 2))))

                # Timer level 3
                self.timer_lvl5 -= self.dt

                self.font = pg.font.Font(None, 30)
                txt = self.font.render("Timer: " + str(round(self.timer_lvl5, 0)), True, black)
                self.screen.blit(txt, (30, 30))

                if self.timer_lvl5 <= 0:
                    self.problemFailed = True

            # Check button
            pg.draw.rect(self.screen, (0, 0, 0), checkButton)

            self.font = pg.font.Font(None, 50)
            labelcheck = self.font.render("Check answer", 1, (255, 255, 255))

            if self.resetStatus:
                print(str(self.timer_reset))
                self.font = pg.font.Font(None, 50)
                labelcheck = self.font.render("Try again!", 1, (255, 0, 0))

                self.timer_reset -= self.dt

                if self.timer_reset <= 0:
                    self.resetStatus = False
                    self.timer_reset = 3
            self.screen.blit(labelcheck, ((checkButton.centerx - (labelcheck.get_rect().width / 2)), (checkButton.centery - (labelcheck.get_rect().height / 2))))

            # Win screen and lose screen
            if self.problemCompleted and self.firstend:

                global completed

                completed = True
                pg.mixer.music.fadeout(200)
                self.win.set_volume(0.5)
                self.win.play(loops=0)
                self.screen.fill(black)
                self.font = pg.font.Font(None, 50)
                label_done_1 = self.font.render("Good job!", 1, (255, 255, 255))
                self.screen.blit(label_done_1, ((400 - (label_done_1.get_rect().width / 2) + 0),(300 - (label_done_1.get_rect().height / 2) - 100)))

                label_done_2 = self.font.render("Press ESCAPE to go back to", 1, (255, 255, 255))
                self.screen.blit(label_done_2, ((400 - (label_done_2.get_rect().width / 2) + 0),(300 - (label_done_2.get_rect().height / 2) - 0)))
                label_done_3 = self.font.render("the main menu.", 1, (255, 255, 255))
                self.screen.blit(label_done_3, ((400 - (label_done_3.get_rect().width / 2) + 0),(300 - (label_done_3.get_rect().height / 2) + 40)))
                self.firstend = False

                # print("COMPLETED")
                # print(str(self.problemCompleted))
            elif self.problemFailed and self.firstend:

                completed = False
                pg.mixer.music.fadeout(200)
                self.lose.set_volume(0.5)
                self.lose.play(loops=0)
                self.screen.fill(black)
                self.font = pg.font.Font(None, 50)
                label_done_1 = self.font.render("You failed!", 1, (255, 255, 255))
                self.screen.blit(label_done_1, ((400 - (label_done_1.get_rect().width / 2) + 0),(300 - (label_done_1.get_rect().height / 2) - 100)))

                label_done_2 = self.font.render("Press ESCAPE to go back to", 1, (255, 255, 255))
                self.screen.blit(label_done_2, ((400 - (label_done_2.get_rect().width / 2) + 0),(300 - (label_done_2.get_rect().height / 2) - 0)))
                label_done_3 = self.font.render("the main menu.", 1, (255, 255, 255))
                self.screen.blit(label_done_3, ((400 - (label_done_3.get_rect().width / 2) + 0),(300 - (label_done_3.get_rect().height / 2) + 40)))
                self.firstend = False

                # print("FAILED")
                # print(str(self.problemFailed))

            pg.display.flip()

            self.dt = self.clock.tick(30) / 1000  # / 1000 to convert to seconds.

class Minigame(object):
    state = True

    # CONSTRUCTOR
    def __init__(self):
        print("LOADING MINIGAME AMAR")
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 100

        self.problem = Problem()

    def render(self):
        #self.screen.fill((12, 75, 22))
        self.problem.render()
        pg.display.flip()

    def main_loop(self):
        Minigame.state = True
        pg.mixer.music.play(loops=1)
        while Minigame.state:
            self.problem.control()
            self.render()
            self.clock.tick(self.fps)

# INIT MINIGAME
def main():
    global completed
    pg.init()
    pg.font.init()
    pg.mixer.init()
    pg.display.set_caption(screen_caption)
    # Delete this for prod
    pg.display.set_mode(screen_size)
    # FULLSCREEN MODE
    # pg.display.set_mode(screen_size, pg.FULLSCREEN)
    pg.mouse.set_visible(1)
    pg.mixer.music.load("minigames/amar/assets/music.mp3")
    pg.mixer.music.set_volume(0.5)
    pg.key.set_repeat(500, 30)
    Minigame().main_loop()
    pg.key.set_repeat(1, 20)
    game = Problem()
    if completed is True:
        print("Player completed the level")
        return True
    elif completed is False:
        print("Player failed the level")
        return False
    else:
        print("err")
    pg.mouse.set_visible(0)


if __name__ == "__main__":
    main()