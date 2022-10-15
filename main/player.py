import pygame
from settings import *

import math


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((32,64))
        
        # temp sprite for testing functionality
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center = pos)
       

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self,dt):
    
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
       
        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
      

    def update(self,dt):
        self.input()
        self.move(dt)


class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,player,group):
        super().__init__(group)
        self.image = pygame.Surface((24,24))
        # temp sprite for testing functionality
        self.circle = pygame.draw.circle(self.image,RED,(12,12),12)
        self.rect = self.image.get_rect(center = pos)
      
        self.player = player
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 75

    def move(self,dt):
        self.direction.x, self.direction.y = self.player.rect.x - self.rect.x, self.player.rect.y - self.rect.y
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
         
    def update(self,dt):
        self.move(dt)