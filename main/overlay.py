import pygame
from support import *
from settings import *

class Overlay:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.font = pygame.font.SysFont('comicsansms',FONT_SIZE['small'],bold = pygame.font.Font.bold)

        overlay_path = PATHS['overlay path']
        x = self.display_surface.get_size()[0] - (HEALTH_BAR_WIDTH + 20)
        y = 20
        self.health_bar_rect = pygame.Rect(x,y,HEALTH_BAR_WIDTH, BAR_HEIGHT)


        self.weapon_graphics = []
        for weapon in weapon_data.values():
            weapon = pygame.image.load(weapon['graphic']).convert_alpha()
            self.weapon_graphics.append(weapon)


        self.qstate_graphics = []
        for qstate in qstate_data.values():
            qstate = pygame.image.load(qstate['graphic']).convert_alpha()
            self.qstate_graphics.append(qstate)



        # this is for side panels on overlay
        self.sketch_surf = pygame.image.load(f"{overlay_path}{OVERLAYS['test']}.png").convert_alpha()
        self.control_surf = pygame.image.load(f"{overlay_path}{OVERLAYS['control_bar']}.png").convert_alpha()


    def show_bar(self,current,max_amount,bg_rect,color):
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

        ratio = current/max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,current_rect,3)

    def show_exp(self,exp):
        text_surf = self.font.render(str(int(exp)),False,'black')
        x = self.display_surface.get_size()[0] -  (WINDOW_WIDTH/2)
        y = 30
        text_rect = text_surf.get_rect(center = (x,y))
        self.display_surface.blit(text_surf,text_rect)
   

    def selection_box(self,left,top,weapon_cooldown):
        bg_rect = pygame.Rect(left,top, ITEM_BOX_SIZE,ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
        if weapon_cooldown and self.player.selected_weapon == 'wing':
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
        else:
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
        return bg_rect

    def weapon_overlay(self, weapon_index,weapon_cooldown):
        
        bg_rect = self.selection_box(SCREEN_WIDTH - (ITEM_BOX_SIZE + 20), SCREEN_HEIGHT - (ITEM_BOX_SIZE + 20),weapon_cooldown)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect =weapon_surf.get_rect(center = bg_rect.center)
        self.display_surface.blit(weapon_surf,weapon_rect)



    def show_controls(self,qstate_index,count):
        if count == 0:
            qstate_surf = self.qstate_graphics[qstate_index]
            qstate_rect = qstate_surf.get_rect(center = CONTROL_BOX[qstate_index])
            self.display_surface.blit(qstate_surf,qstate_rect)





    def display(self):
        # pygame.draw.rect(self.display_surface,'black',self.health_bar_rect)
        self.show_bar(self.player.health,self.player.stats['health'],self.health_bar_rect,'red')
        self.show_exp(self.player.level)
        self.weapon_overlay(self.player.weapon_index,self.player.timers['weapon cooldown'].active)
        self.show_controls(self.player.controls.model.qin,self.player.controls.count)

        # self.health_surf = pygame.transform.scale(self.health_surf,(232,45))
        # self.health_rect = self.health_surf.get_rect(midtop=OVERLAY_POSITIONS['health bar'])

        self.sketch_surf = pygame.transform.scale(self.sketch_surf,(225,400))
        self.sketch_rect = self.sketch_surf.get_rect(topleft= OVERLAY_POSITIONS['sketch'])
        
        self.control_surf = pygame.transform.scale(self.control_surf,(225,175))
        self.control_rect = self.control_surf.get_rect(topleft = OVERLAY_POSITIONS['control'])

        # self.display_surface.blit(self.health_surf,self.health_rect)
        self.display_surface.blit(self.sketch_surf,self.sketch_rect)
        self.display_surface.blit(self.control_surf,self.control_rect)