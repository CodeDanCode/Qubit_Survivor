import pygame
from settings import *
from player import *
from overlay import *
from sprites import Generic
from pytmx.util_pygame import load_pygame
import random

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        tmx_data = load_pygame(PATHS['data path'])
        
        # Map collision 
        for x,y,surf in tmx_data.get_layer_by_name('collision').tiles():
            Generic((x*TILE_SIZE,y*TILE_SIZE), pygame.Surface((TILE_SIZE,TILE_SIZE)), self.collision_sprites)
           
        self.player = Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2),self.all_sprites,self.collision_sprites)
        
        Generic(
            pos = (0,0),
            surf = pygame.image.load('../resources/assets/map.png').convert_alpha(), # change to settings variable here 
            groups = self.all_sprites,
            z = LAYERS['ground']
        )
       
        Spawn(self.player,[self.all_sprites,self.collision_sprites])
        
        # self.enemy = Enemy((100,100),self.player,[self.all_sprites,self.collision_sprites])
        # self.enemy = Enemy((100,200),self.player,[self.all_sprites,self.collision_sprites])
        
        # self.enemy = Enemy((loc,loc),self.player,self.all_sprites)
        # self.enemy = Enemy((loc*2,loc),self.player,self.all_sprites)

    def run(self, dt):
        self.display_surface.fill(COLORS['blue'])
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.overlay.display()

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.custom_surface = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.offset = pygame.math.Vector2()


    def custom_draw(self, player):
        # self.offset.x = (player.rect.centerx - SCREEN_WIDTH / 2)
        # self.offset.y = (player.rect.centery - SCREEN_HEIGHT / 2)
        self.offset.x = (player.rect.centerx - WINDOW_WIDTH/2)
        self.offset.y = (player.rect.centery - WINDOW_HEIGHT/2)

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.custom_surface.blit(sprite.image,offset_rect)
                    self.display_surface.blit(self.custom_surface,(240,5))