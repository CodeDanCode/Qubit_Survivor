import pygame
from settings import *
from model import *

class Controls:
    def __init__(self,player,group):
        self.count = 0
        self.player =player
        self.model = CircuitGridModel()
        self.fighting = False
        self.stop = False
        self.qstate = None
        
    
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

        # keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if not self.player.timers['weapon use'].active:
                    if event.key == pygame.K_h:
                        self.model.add_to_circuit('H',self.count, self.fighting)
                        self.count+=1
                    elif event.key == pygame.K_i:
                        self.model.add_to_circuit('I',self.count, self.fighting)
                        self.count+=1        
                    elif event.key == pygame.K_y:
                        self.model.add_to_circuit('Y',self.count, self.fighting)
                        self.count+=1



                    elif event.key == pygame.K_SPACE:
                        self.qstate = None

                    
                    if self.count >=3 and not self.fighting:
                        self.qstate = self.model.collapse(self.model.qwl)
                        self.set_direction()
                        self.count = 0

                    if self.qstate == None:
                        self.player.direction = pygame.math.Vector2()



    def set_direction(self):
        

        if self.qstate == '000':
            self.player.direction.x = -1
            self.player.status = UP

        self.model.update()


        
    