import pygame
from support import *
from settings import *

class Overlay:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        # self.font = pygame.font.Font('comicsansms',FONT_SIZE)

        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH, BAR_HEIGHT)
        # self.health_bar_rect = pygame.Rect(OVERLAY_POSITIONS['health bar'][0],OVERLAY_POSITIONS['health bar'][1],HEALTH_BAR_WIDTH, BAR_HEIGHT)


        # import overlays
        overlay_path = PATHS['overlay path']
        # self.health_surf = pygame.image.load(f"{overlay_path}{OVERLAYS['health bar']}.png").convert_alpha()
        # self.sketch_surf = pygame.image.load(f"{overlay_path}{OVERLAYS['sketch']}.png").convert_alpha()
    
    def show_bar(self,current,max_amount,bg_rect,color):
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

        ratio = current/max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,current_rect,3)

    def display(self):
        # pygame.draw.rect(self.display_surface,'black',self.health_bar_rect)
        self.show_bar(self.player.health,self.player.stats['health'],self.health_bar_rect,'red')

        # self.health_surf = pygame.transform.scale(self.health_surf,(232,45))
        # self.health_rect = self.health_surf.get_rect(midtop=OVERLAY_POSITIONS['health bar'])

        # self.sketch_surf = pygame.transform.scale(self.sketch_surf,(225,400))
        # self.sketch_rect = self.sketch_surf.get_rect(topleft= OVERLAY_POSITIONS['sketch'])

        # self.display_surface.blit(self.health_surf,self.health_rect)
        # self.display_surface.blit(self.sketch_surf,self.sketch_rect)