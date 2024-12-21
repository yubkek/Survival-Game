import pygame
from settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((ENTITY_SIZE, ENTITY_SIZE)), position = (0,0)):
        super().__init__(groups)
        self.image = image
        self.image = pygame.image.load("images/s2.png")
        self.image = pygame.transform.scale(self.image, (ENTITY_SIZE, ENTITY_SIZE))
        self.rect = self.image.get_frect(topleft = position)