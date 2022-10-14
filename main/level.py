import pygame
from settings import *
from player import *
import random

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.setup()


    def setup(self):
        self.player = Player((600,300),self.all_sprites)
        loc = random.randrange(600)
        self.enemy = Enemy((100,100),self.all_sprites)
        self.enemy = Enemy((loc,loc),self.all_sprites)
        self.enemy = Enemy((loc*100,loc),self.all_sprites)


           
    def run(self, dt):
        self.display_surface.fill(BLACK)
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt,self.player)