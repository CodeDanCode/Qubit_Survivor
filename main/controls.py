import pygame
from settings import *
from model import *

class Controls:
    def __init__(self,player):
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
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if not self.player.timers['weapon use'].active:
                    if event.key == pygame.K_h:
                        self.model.add_to_circuit('H',self.count, self.fighting)
                        self.count+=1
                    elif event.key == pygame.K_i:
                        self.model.add_to_circuit('I',self.count, self.fighting)
                        self.count+=1    
                    elif event.key == pygame.K_s:
                        self.model.add_to_circuit('S',self.count, self.fighting)
                        self.count+=1
                    elif event.key == pygame.K_t:
                        self.model.add_to_circuit('T',self.count, self.fighting)
                        self.count+=1
                    elif event.key == pygame.K_x:
                        self.model.add_to_circuit('X',self.count, self.fighting)
                        self.count+=1
                    elif event.key == pygame.K_y:
                        self.model.add_to_circuit('Y',self.count, self.fighting)
                        self.count+=1
                    elif event.key == pygame.K_z:
                        self.model.add_to_circuit('Z',self.count, self.fighting)
                        self.count+=1

                    # stop movement
                    elif event.key == pygame.K_SPACE:
                        self.qstate = None


                    elif event.key == pygame.K_LSHIFT:
                        self.fighting = True

                    
                    if self.count >=3 and not self.fighting:
                        self.qstate = self.model.collapse(self.model.qwl)
                        self.set_direction()
                        self.count = 0

                    elif self.count >=2 and self.fighting:
                        self.qstate = self.model.collapse(self.model.qwlf)
                        print("fighting: ", self.qstate)
                        self.set_fighting()
                        self.count = 0

                    if self.qstate == None:
                        self.player.direction = pygame.math.Vector2()





    def set_direction(self):
        # north
        if self.qstate == '000':
            self.player.direction.y = -1
            self.player.status = UP
        # north east
        if self.qstate == '001':
            self.player.direction.y = -1
            self.player.direction.x = 1
            self.player.status = RIGHT

        # east
        if self.qstate == '010':
            self.player.direction.x = 1
            self.player.status = RIGHT
        # south east
        if self.qstate == '011':
            self.player.direction.y = 1
            self.player.direction.x = 1
            self.player.status = RIGHT
        # south
        if self.qstate == '100':
            self.player.direction.y = 1
            self.player.status = DOWN
        # south west
        if self.qstate == '101':
            self.player.direction.y = 1
            self.player.direction.x = -1
            self.player.status = LEFT 
        # west
        if self.qstate == '110':
            self.player.direction.x = -1
            self.player.status = LEFT
        # north west
        if self.qstate == '111':
            self.player.direction.y = -1
            self.player.direction.x = -1
            self.player.status = LEFT

        self.model.update()
       

    def set_fighting(self):
        if not self.player.timers['weapon switch'].active:
            
            if self.qstate == '00' or self.qstate == '11':
                self.player.weapon_index = 0
                self.player.selected_weapon = self.player.weapons[self.player.weapon_index]


            elif self.qstate == '10' or self.qstate == '01':
                self.player.weapon_index = 1
                self.player.selected_weapon = self.player.weapons[self.player.weapon_index]

        self.player.timers['weapon use'].activate()
        self.player.direction = pygame.math.Vector2()
        self.player.frame_index = 0
        self.model.update()
        self.fighting = False
      