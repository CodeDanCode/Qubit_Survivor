import pygame, sys, os
from level import *
from settings import *
from menu import *
from qiskit import IBMQ
from dotenv import load_dotenv

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.connect()
        self.menu = Menu()

    def connect(self):
        load_dotenv()
        TOKEN = os.getenv('TOKEN')
        IBMQ.save_account(TOKEN)

        IBMQ.load_account() # opens account to get access to backends
        provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
        backend = provider.get_backend('ibmq_manila') # random backend

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
            self.menu.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Main()
    game.run()