import pygame
import config
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.playerSurf = pygame.Surface((50,50))
        self.rect = pygame.draw.rect(self.playerSurf,(255,0,0),pygame.Rect(50,50,50,50))
        

    def updated(self):
        pygame.display.flip()





class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    


    def updated(self):
        pygame.display.flip()