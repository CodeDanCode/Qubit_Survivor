import pygame
from settings import *
from support import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,player,group,type):
        super().__init__(group)
        
        self.enemy_type = type
        self.group = group


        self.import_assets()
        self.status = 'right_idle'
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']
      
        self.player = player
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 75

        self.health = 25


        self.hitbox = self.rect.copy().inflate((-60,0))
        self.attackbox = self.rect.copy()
        self.enemyHitbox = self.rect.copy()

        self.collide = False        

    def import_assets(self):
        self.animations = {'left_idle':[],'left':[],'right_idle':[],'right':[]}
        for animation in self.animations.keys():
            full_path = PATHS['enemy base']+ self.enemy_type +"/"+ animation
            self.animations[animation] = import_folder(full_path)
    
    def animate(self,dt):
        self.frame_index +=4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def get_status(self):

        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + "_idle"
        
    def collision(self,direction):
        for sprite in self.group[0].sprites():
            if sprite == self.player:
                if sprite.enemybox.colliderect(self.hitbox):
                    self.direction = pygame.math.Vector2() 
                    if direction == 'horizontal':
                        if self.direction.x > 0:
                            self.hitbox.right = sprite.enemybox.left
                        if self.direction.x < 0: 
                            self.hitbox.left = sprite.enemybox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                    
                    if direction == 'vertical':
                          
                        if self.direction.y > 0:
                            self.hitbox.bottom = sprite.enemybox.top
                        if self.direction.y < 0:
                            self.hitbox.top = sprite.enemybox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery


    def move(self,dt):
        

        self.direction.x, self.direction.y = self.player.rect.x - self.rect.x, self.player.rect.y - self.rect.y
  
        
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        #horizontal movement
        if self.rect.x > self.player.rect.x:
            self.status = LEFT
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.attackbox.centerx = round(self.pos.x)
        self.enemyHitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.attackbox.centerx
        self.collision('horizontal')
    
        
        #vertical movement
        if self.rect.x < self.player.rect.x:
            self.status = RIGHT
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.attackbox.centery = round(self.pos.y)
        self.enemyHitbox.centery = round(self.pos.y)
        self.rect.centery = self.attackbox.centery
        self.collision('vertical')


    def damage(self):
        self.health -= self.player.attack + weapon_data[self.player.selected_weapon]['damage']

        if self.health <= 0:
            self.kill()

    def update(self,dt):
        self.get_status()
        self.move(dt)
        self.animate(dt)



        