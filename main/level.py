import pygame
from settings import *
from player import *
from overlay import *
from sprites import Generic
import random

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        
        self.player = Player((600,300),self.all_sprites,self.collision_sprites)
        
        Generic(
            pos = (0,0),
            surf = pygame.image.load('../resources/assets/ground.png').convert_alpha(), # change to settings variable here 
            groups = self.all_sprites,
            z = LAYERS['ground']
        )
       
        



        self.enemy = Enemy((100,100),self.player,self.all_sprites)
        # self.enemy = Enemy((loc,loc),self.player,self.all_sprites)
        # self.enemy = Enemy((loc*2,loc),self.player,self.all_sprites)

    def run(self, dt):
        self.display_surface.fill(COLORS['black'])
        # self.all_sprites.draw(self.display_surface)
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

        self.overlay.display()

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()


    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image,offset_rect)