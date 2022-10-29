import pygame, sys
from level import *
from settings import *


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            dt = self.clock.tick() /1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Main()
    game.run()