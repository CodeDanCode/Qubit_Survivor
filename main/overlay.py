import pygame
from support import *
from settings import *

class Overlay:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        # import overlays
        overlay_path = PATHS['overlay path']
        self.health_surf = pygame.image.load(f"{overlay_path}{OVERLAYS['health bar']}.png").convert_alpha()
        self.sketch_surf = pygame.image.load(f"{overlay_path}{OVERLAYS['sketch']}.png").convert_alpha()
    
    def display(self):
       
        self.health_surf = pygame.transform.scale(self.health_surf,(232,45))
        self.health_rect = self.health_surf.get_rect(midtop=OVERLAY_POSITIONS['health bar'])

        self.sketch_surf = pygame.transform.scale(self.sketch_surf,(225,400))
        self.sketch_rect = self.sketch_surf.get_rect(topleft= OVERLAY_POSITIONS['sketch'])

        self.display_surface.blit(self.health_surf,self.health_rect)
        self.display_surface.blit(self.sketch_surf,self.sketch_rect)