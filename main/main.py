import pygame, sys
from level import *
from settings import *
from menu import *
from qiskit import IBMQ

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        # self.level = Level()
        self.connect()
        self.menu = Menu()

    def connect(self):
        #
        ACC_KEY = '87fe2c4d836339dafc11fe4589a3d0a55f3fbc87da611c4c7ebc7a9e43895736fd5360b29c02fb7102421c9ef18ae17e307a56e03f6a4cfda3da047c5bba16f2'
        IBMQ.save_account(ACC_KEY)

        IBMQ.load_account() # opens account to get access to backends
        provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
        backend = provider.get_backend('ibmq_manila') # random backend

        # pretends to create the circuit 
        qoutput = "Creating circuit..."
        # print(qoutput)

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
            # self.level.run(dt)
            self.menu.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Main()
    game.run()