import pygame
from settings import *
from pytmx.util_pygame import load_pygame
from player import Player
from monster import Monster
from tiles import Tile
from groups import *

class Scene:
    def __init__(self, app):
        self.app = app

        # all
        self.allSprites = AllSprites()

        # map
        self.grassTiles = GrassTiles()
        self.fallTiles = FallTiles()
        self.blockTiles = BlockTiles()

        self.importAssets()
        self.setup(self.map['world'])
        
        # player
        self.playerSprite = PlayerSprite()
        self.player = Player([self.allSprites, self.playerSprite])

        # monsters
        self.monsterSprites = EnemySprites()
        Monster([self.allSprites, self.monsterSprites])
    
    def importAssets(self):
        self.map = {
            'world' : load_pygame('assets/map.tmx'),
        }

    def setup(self, map):
        for x, y, surf in map.get_layer_by_name('Grass').tiles():
            Tile([self.allSprites, self.grassTiles], surf, (x * TILESIZE, y * TILESIZE))
        for x, y, surf in map.get_layer_by_name('Fall').tiles():
            Tile([self.allSprites, self.fallTiles], surf, (x * TILESIZE, y * TILESIZE))
        for x, y, surf in map.get_layer_by_name('Block').tiles():
            Tile([self.allSprites, self.blockTiles], surf, (x * TILESIZE, y * TILESIZE))

    def update(self, dt):
        self.playerSprite.update(dt)

    def draw(self):
        self.app.screen.fill("cadetblue1")
        self.allSprites.draw(self.player.rect.center)