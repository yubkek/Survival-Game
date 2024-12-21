import pygame
from settings import *
from scene import Scene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.scene = Scene(self)
    
    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        dt = self.clock.tick() / 1000
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.running = False
        
        self.scene.update(dt)
        pygame.display.update()

    def draw(self):
        self.scene.draw()

    def close(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()