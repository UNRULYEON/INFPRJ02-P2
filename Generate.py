import pygame as py
from Object import Object

#Generate class
class Generate:
    def __init__(self,spritegroup):
        self.a = [					(200,0),(275,0),(350,0),
                					(200,75),(275,75),(350,75),
                (50,150),(125,150),(200,150),(275,150),(350,150),(425,150),(500,150),
                (50,225),(125,225),(200,225),(275,225),(350,225),(425,225),(500,225),
                (50,300),(125,300),(200,300),(275,300),(350,300),(425,300),(500,300),
                					(200,375),(275,375),(350,375),
                					(200,450),(275,450),(350,450)]
        for x in self.a:
            Object("Resources/ball.png",x[0],x[1] ,spritegroup)
    def update(self):
        pass
