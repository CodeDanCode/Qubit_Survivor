import pygame
from settings import *
from support import *
from timers import Timer
from controls import *
from enemy import Enemy
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group,collision_sprites,enemy_sprites):
        super().__init__(group)
        self.import_assets()
        self.controls = Controls(self)
        self.game_over = False
        self.group = [group,collision_sprites,enemy_sprites]
        self.enemy_index = 0
        self.status = 'right_idle'
        self.frame_index = 0 
        self.temp_player(pos)
        self.z = LAYERS['main']

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

        self.stats = {'health':100 , 'attack': 10,'speed': 200, 'level': 1, 'exp':100}
        self.maxstats = {'health':200,'attack':20, 'speed': 300, 'exp':10000}
        self.health = self.stats['health'] 
        self.attack = self.stats['attack']
        self.exp = self.stats['exp']
        self.speed = self.stats['speed']
        self.level = self.stats['level']
        
        self.target_rect = None

        self.hitbox = self.rect.copy()
        self.attackbox = self.rect.copy().inflate(self.rect.width * 20, self.rect.width * 20)

        # self.enemybox = self.rect.copy().inflate(self.rect.width * 2, self.rect.height *2)
        self.enemybox = self.rect.copy()


        self.collision_sprites = collision_sprites
        self.enemy_sprites = enemy_sprites

        self.timers = {
                'weapon use': Timer(350, self.use_weapon),
                'weapon switch': Timer(200),
                'weapon cooldown' : Timer(15000)
            }
        
        self.weapons = ['hoot','wing'] # add wing when ready
        self.weapon_index = 0
        self.selected_weapon = self.weapons[self.weapon_index]

    def temp_player(self,pos):
         # general sprite setup  
        self.image = pygame.Surface((16,32)) # remove temp surface 
        self.image.fill(COLORS['red']) # remove surface fill
        # use below for player sprite animation when recieved
        # self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)  
        

    def import_assets(self):
        self.animations = {'up':[],'up_idle':[],'down':[],'down_idle':[],'left':[],'left_idle':[],'right':[],'right_idle':[],
                            'left_hoot':[],'left_wing':[],'right_hoot':[],'right_wing':[]}

        for animation in self.animations.keys():
            full_path = PATHS['player base'] + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self,dt):
        self.frame_index +=4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]


    def use_weapon(self):
        if self.selected_weapon == 'hoot':
            for enemy in self.enemy_sprites.sprites():
                if enemy.rect.collidepoint(self.target_pos):
                    # print(self.attack + weapon_data[self.selected_weapon]['damage'])
                    enemy.damage()

        if self.selected_weapon == 'wing' and not self.timers['weapon cooldown'].active:
            for enemy in self.enemy_sprites.sprites():
                if enemy.rect.colliderect(self.attackbox):
                        enemy.damage()
                        self.timers['weapon cooldown'].activate()



    def get_target_pos(self):
        if self.selected_weapon == 'hoot':
            self.target_pos = self.rect.center + PLAYER_HOOT_OFFSET[self.status.split('_')[0]]

        if self.selected_weapon == 'wing':
            self.target_pos = self.rect.center + PLAYER_WING_OFFSET[self.status.split('_')[0]]

    def control(self,selected):
        self.selected = selected
        if self.selected == 'easy':
            self.controls.easy_controls()
        if self.selected == 'normal':
            pass
        if self.selected == 'hard':
            self.controls.hard_controls()

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + "_idle"
            # self.status += '_idle'

        if self.timers['weapon use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_weapon
  

        if self.exp >= 1000 * self.level:
            self.levelup()

    
    def levelup(self):
        self.level += 1
        self.health += 10
        self.attack += 1
        self.speed += 10
        
        if (self.level % 2) != 0 and self.enemy_index <=3:
            self.enemy_index += 1

        elif self.enemy_index == 3:
            self.enemy_index = 0


    def collision(self,direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite,'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0:
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0: 
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                    
                    if direction == 'vertical':    
                        if self.direction.y > 0:
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery
            if hasattr(sprite,'enemybox'):
                if sprite.enemybox.colliderect(self.attackbox):
                    sprite.speed_status = True
                else:
                    sprite.speed_status = False

    def move(self,dt):
    
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.attackbox.centerx = round(self.pos.x)
        self.enemybox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.attackbox.centery = round(self.pos.y)
        self.enemybox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self,dt,selected):
        # self.input()
        self.control(selected)
        self.get_status()
        self.update_timers()
        self.get_target_pos()
        self.move(dt)
        
        # self.animate(dt)





        