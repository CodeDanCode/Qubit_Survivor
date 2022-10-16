import pygame
from settings import *
from timer import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.status = 'idle'
        self.frame_index = 0

        self.image = pygame.Surface((32,64))    
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center = pos)
    
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
        self.timers = {'attack use': Timer(350, self.use_attack),'player turn': Timer(5000)}
        self.selected_attack = 'hoot'

    def use_attack(self):
        # print(self.selected_attack)
        pass
        
    def input(self):
        keys = pygame.key.get_pressed()
        if not self.timers['attack use'].active or not self.timers['player turn'].active:
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            if keys[pygame.K_SPACE]:
                self.timers['attack use'].activate()
                self.direction = pygame.math.Vector2()

            # if keys[pygame.K_q]:
            #     self.timers['player turn'].activate()

    def get_status(self):


        if self.timers['attack use'].active:
            print("attack is be used")
        
        if self.timers['player turn'].active:
            print("player turn: " + str(self.timers['player turn'].active))
    
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

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
        self.get_status()
        self.update_timers()
        self.move(dt)
        # Add animation function here


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