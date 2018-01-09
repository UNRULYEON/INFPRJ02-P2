import pygame as py
from Object import Object
###           0 ,1 ,2
###           3 ,4 ,5
###     6 ,7 ,8 ,9 ,10,11,12,
###     13,14,15,16,17,18,19
###     20,21,22,23,24,25,26
###           27,28,29
###           30,31,32
# Generate class
class Generate:
    def __init__(self,spritegroup):
        self.a = [					(270,0),(355,0),(440,0),
                					(270,85),(355,85),(440,85),
                (100,170),(185,170),(270,170),(355,170),(440,170),(525,170),(610,170),
                (100,255),(185,255),(270,255),(355,255),(440,255),(525,255),(610,255),
                (100,340),(185,340),(270,340),(355,340),(440,340),(525,340),(610,340),
                					(270,425),(355,425),(440,425),
                					(270,510),(355,510),(440,510)]
        self.level1 = [4, 8, 9, 10, 16, 23]
        self.b = []
        self.c = []
        for x in range (0,32):
            self.b.append(False)
        self.occupied = []
        for y in self.level1:
            self.spawn(y, spritegroup)
        print(len(self.occupied))

    def update(self):
        pass

    def spawn(self, position, spritegroup):
        if not self.b[position]:
            self.c.insert(position, Object("Resources/ball.png", self.a[position][0], self.a[position][1], spritegroup))
            self.b[position] = True
            self.occupied.insert(position, position)
        else:
            print("already spawned")

    def despawn(self, position):
        self.c[position].end()
        self.b[position] = False
        self.occupied.pop(position)
        pass
