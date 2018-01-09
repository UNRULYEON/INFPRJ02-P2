import os, sys
import pygame as pg

def asset(name):
    fullname = os.path.join("assets", name)
    # try:
    image = pg.image.load(fullname)
    #     if image.get_alpha is None:
    #         image = image.convert()
    #     else:
    #         image = image.convert_alpha()
    # except pg.error:
    #     logging.info("Cannot load image: " + fullname)
    #     print("Cannot load image: " + fullname)
    #     raise SystemExit
    return image, image.get_rect()