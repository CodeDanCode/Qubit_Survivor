import pygame
from support import *
from settings import *

class Overlay:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        # health overlay
        overlay_path = PATHS['overlay path']
        self.health_surf = {'health bar': pygame.image.load(f"{overlay_path}{OVERLAYS['health bar']}.png").convert_alpha()}
        # sketch overlay

        # control overlay

    
    def display(self):
        health_surf = self.health_surf['health bar']
        health_surf = pygame.transform.scale(health_surf,(232,45))
        health_rect = health_surf.get_rect(midbottom=OVERLAY_POSITIONS['health bar'])
        self.display_surface.blit(health_surf,health_rect)