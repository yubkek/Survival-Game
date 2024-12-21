import pygame
from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def draw(self, playerCenter):
        self.offset.x = -(playerCenter[0] - SCREEN_WIDTH/2)
        self.offset.y = -(playerCenter[1] - SCREEN_HEIGHT/2)

        for sprite in self:
            self.displaySurface.blit(sprite.image, sprite.rect.topleft + self.offset)

class PlayerSprite(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

class EnemySprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

class GrassTiles(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

class FallTiles(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

class BlockTiles(pygame.sprite.Group):
    def __init__(self):
        super().__init__()