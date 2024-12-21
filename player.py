import pygame
import math
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((ENTITY_SIZE, ENTITY_SIZE)), position = (0,0)):
        super().__init__(groups)
        self.image = pygame.image.load("assets/Player.png")
        self.image = pygame.transform.scale(self.image, (ENTITY_SIZE, ENTITY_SIZE))
        self.rect = self.image.get_frect(topleft = position)
        self.direction = pygame.math.Vector2()

    def update(self, dt):
        self.input()
        self.move(dt)

    def input(self):
        keys = pygame.key.get_pressed()

        inputVector = pygame.math.Vector2()

        if (keys[pygame.K_w]):
            if not self.rect.y - 3 < 0:
                inputVector.y -= 3
            else:
                inputVector.y = 0
        if (keys[pygame.K_a]):
            if not self.rect.x - 3 < 0:
                inputVector.x -= 3
            else:
                inputVector.x = 0
        if (keys[pygame.K_s]):
            if not self.rect.y + 3 > (30 * TILESIZE):
                inputVector.y += 3
            else:
                self.rect.y = 30 * TILESIZE
                inputVector.y = 0 
        if (keys[pygame.K_d]):
            if not self.rect.x + 3 > (34 * TILESIZE):
                inputVector.x += 3
            else:
                self.rect.x = 34 * TILESIZE
                inputVector.x = 0 
        self.direction = inputVector

        if keys[pygame.K_l]:
            print(self.rect.x, self.rect.y)

    def move(self, dt):
        self.rect.center += self.direction * 150 * dt