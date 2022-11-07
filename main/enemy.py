import pygame
from settings import *
from support import *
from timers import Timer


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
        self.speed_status = False
        # self.stats = {'health': 25,'speed': 75, 'damage':25}

        self.speed = ENEMY_DATA[self.enemy_type]['speed']
        self.health = ENEMY_DATA[self.enemy_type]['health']


        # self.hitbox = self.rect.copy().inflate((-60,0))
        # self.attackbox = self.rect.copy()
        self.enemybox = self.rect.copy()

        self.timers = {
            'attack': Timer(1000,self.attack)
        }

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

        if self.speed_status == True:
            self.speed = ENEMY_DATA[self.enemy_type]['speed'] * 0.5
        else:
            self.speed = ENEMY_DATA[self.enemy_type]['speed']
        
    def collision(self,direction):
        for sprite in self.group[0].sprites():
            if sprite == self.player:
                if sprite.hitbox.colliderect(self.enemybox):
                    self.direction = pygame.math.Vector2() 
                    if not self.timers['attack'].active:
                        self.timers['attack'].activate()                
                    if direction == 'horizontal':
                        if self.direction.x > 0:
                            self.enemybox.right = sprite.enemybox.left
                        if self.direction.x < 0: 
                            self.enemybox.left = sprite.enemybox.right
                        self.rect.centerx = self.enemybox.centerx
                        self.pos.x = self.enemybox.centerx
                    
                    if direction == 'vertical':
                        if self.direction.y > 0:
                            self.enemybox.bottom = sprite.enemybox.top
                        if self.direction.y < 0:
                            self.enemybox.top = sprite.enemybox.bottom
                        self.rect.centery = self.enemybox.centery
                        self.pos.y = self.enemybox.centery

                    


    def move(self,dt):
        

        # self.direction.x, self.direction.y = self.player.rect.x - self.rect.x, self.player.rect.y - self.rect.y

        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(self.player.rect.center)
        # self.direction = (player_vec - enemy_vec).normalize()
        self.direction = player_vec - enemy_vec
        
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        if self.rect.x > self.player.rect.x:
            self.status = LEFT
        if self.rect.x < self.player.rect.x:
            self.status = RIGHT

        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        # self.attackbox.centerx = round(self.pos.x)
        self.enemybox.centerx = round(self.pos.x)
        # self.rect.centerx = self.attackbox.centerx
        self.rect.centerx = self.enemybox.centerx
        self.collision('horizontal')
    
        
        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        # self.attackbox.centery = round(self.pos.y)
        self.enemybox.centery = round(self.pos.y)
        # self.rect.centery = self.attackbox.centery
        self.rect.centery = self.enemybox.centery
        self.collision('vertical')
 

    def attack(self):
        self.player.health -= ENEMY_DATA[self.enemy_type]['damage']

        if self.player.health <= 0:
            self.player.kill()
            self.player.game_over = True


    def damage(self):
        self.health -= self.player.attack + weapon_data[self.player.selected_weapon]['damage']

        if self.health <= 0:
            self.kill()

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self,dt,selected):
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)



        