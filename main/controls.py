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
                self.timers['weapon use'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0

            if keys[pygame.K_e] and not self.timers['weapon switch'].active:
                self.timers['weapon switch'].activate()
                self.weapon_index +=1
                self.weapon_index = self.weapon_index if self.weapon_index < len(self.weapons) else 0
                self.selected_weapon = self.weapons[self.weapon_index]

    def medium_contorls(self):
        pass
    def hard_controls(self):
        pass

