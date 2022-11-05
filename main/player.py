import pygame
from settings import *
from support import *
from timers import Timer
from controls import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group,collision_sprites,enemy_sprites):
        super().__init__(group)
        self.import_assets()
        self.controls = Controls(self)

        self.status = 'right_idle'
        self.frame_index = 0 
        self.temp_player(pos)
        self.z = LAYERS['main']

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

        self.stats = {'health':100 , 'attack': 10,'speed': 200, 'level': 1, 'exp':100}
        self.health = self.stats['health'] 
        self.attack = self.stats['attack']
        self.exp = self.stats['exp']
        self.speed = self.stats['speed']
        self.level = self.stats['level']




        self.hitbox = self.rect.copy()
        self.attackbox = self.rect.copy().inflate(self.rect.width * 20, self.rect.width * 20)
        self.enemybox = self.rect.copy().inflate(self.rect.width * 2, self.rect.height *2)

        self.collision_sprites = collision_sprites
        self.enemy_sprites = enemy_sprites

        self.timers = {
                'weapon use': Timer(350, self.use_weapon),
                'weapon switch': Timer(200)
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
                    print(self.attack + weapon_data[self.selected_weapon]['damage'])
                    enemy.damage()

        if self.selected_weapon == 'wing':
            for enemy in self.enemy_sprites.sprites():
                if enemy.rect.collidepoint(self.target_pos):
                    if enemy.rect.collidepoint(self.target_pos):
                        enemy.damage()

    def get_target_pos(self):
        if self.selected_weapon == 'hoot':
            self.target_pos = self.rect.center + PLAYER_HOOT_OFFSET[self.status.split('_')[0]]
        if self.selected_weapon == 'wing':
            self.target_pos = self.rect.center + PLAYER_WING_OFFSET[self.status.split('_')[0]]

    def control(self,selected):
        if selected == 'easy':
            self.controls.easy_controls()
        if selected == 'normal':
            pass
        if selected == 'hard':
            pass

    # def input(self):
    #     keys = pygame.key.get_pressed()
    #     if not self.timers['weapon use'].active:
    #         if keys[pygame.K_UP]:
    #             self.direction.y = -1
    #             self.status = UP
    #         elif keys[pygame.K_DOWN]:
    #             self.direction.y = 1
    #             self.status = DOWN
    #         else:
    #             self.direction.y = 0

    #         if keys[pygame.K_RIGHT]:
    #             self.direction.x = 1
    #             self.status = RIGHT
    #         elif keys[pygame.K_LEFT]:
    #             self.direction.x = -1
    #             self.status = LEFT
    #         else:
    #             self.direction.x = 0

    #         if keys[pygame.K_SPACE]:
    #             self.timers['weapon use'].activate()
    #             self.direction = pygame.math.Vector2()
    #             self.frame_index = 0

    #         if keys[pygame.K_e] and not self.timers['weapon switch'].active:
    #             self.timers['weapon switch'].activate()
    #             self.weapon_index +=1
    #             self.weapon_index = self.weapon_index if self.weapon_index < len(self.weapons) else 0
    #             self.selected_weapon = self.weapons[self.weapon_index]

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + "_idle"
            # self.status += '_idle'

        if self.timers['weapon use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_weapon
  

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





        