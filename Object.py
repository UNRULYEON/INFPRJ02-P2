import pygame


# Object class
class Object(pygame.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.rect.center = (pos_x / 2, pos_y / 2)

    def update(self):
        pass
