import pygame
from settings import *

class Controls:
    def __init__(self,player):
        self.player =player
    
    def easy_controls(self):
        keys = pygame.key.get_pressed()
        if not self.player.timers['weapon use'].active:
            if keys[pygame.K_UP]:
                self.player.direction.y = -1
                self.player.status = UP
            elif keys[pygame.K_DOWN]:
                self.player.direction.y = 1
                self.player.status = DOWN
            else:
                self.player.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.player.direction.x = 1
                self.player.status = RIGHT
            elif keys[pygame.K_LEFT]:
                self.player.direction.x = -1
                self.player.status = LEFT
            else:
                self.player.direction.x = 0

            if keys[pygame.K_SPACE]:
                self.player.timers['weapon use'].activate()
                self.player.direction = pygame.math.Vector2()
                self.player.frame_index = 0

            if keys[pygame.K_e] and not self.player.timers['weapon switch'].active:
                self.player.timers['weapon switch'].activate()
                self.player.weapon_index +=1
                self.player.weapon_index = self.player.weapon_index if self.player.weapon_index < len(self.player.weapons) else 0
                self.player.selected_weapon = self.player.weapons[self.player.weapon_index]

    def medium_contorls(self):
        pass
    def hard_controls(self):
        pass

