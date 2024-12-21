import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, surf, position):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = position)