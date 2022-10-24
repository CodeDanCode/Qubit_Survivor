import pygame
from settings import *
from support import *
from timer import Timer
from attack import *
import random




class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group,collision_sprites):
        super().__init__(group)
        self.import_assets()
        self.status = '_idle'
        self.frame_index = 0 
        self.pos = pos
        # general sprite setup  
        self.image = pygame.Surface((32,64)) # remove temp surface 
        self.image.fill(COLORS['red']) # remove surface fill
        # self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)  
        self.z = LAYERS['main']

        # character movement variables
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
        self.timers = {
            USE_ATTACK: Timer(350, self.use_attack),
            PLAYER_TURN: Timer(200)
            }

        self.selected_attack = 'hoot'

        # collision boxes
        self.hitbox = self.rect.copy()
        self.attackbox = self.rect.copy().inflate(self.rect.width * 4, self.rect.height * 4)
        self.collision_sprites = collision_sprites
        self.group = group

    def import_assets(self):
        self.animations = {'_idle':[],'up':[],'down':[],'left':[],'right':[],
                            'left_attack':[],'right_attack':[]}

        for animation in self.animations.keys():
            full_path = PATHS['player base'] + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self,dt):
        self.frame_index +=4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def use_attack(self):
        # print(self.selected_attack)
        pass
        
    def input(self):
        keys = pygame.key.get_pressed()
        # control for player movement
        # condition on player_turn and attack turn status
        # control for attack selection 
        # condition attack selection based on and 
        #
        # if not self.timers[USE_ATTACK].active: 
        #  change if for player turn to not allow players to move. 
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = UP
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = DOWN
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = LEFT
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = RIGHT
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.timers[USE_ATTACK].activate()
            self.direction = pygame.math.Vector2()

        # if keys[pygame.K_q] and not self.timers[player_turn].active:
        #     self.timers[player_turn].activate()
        #     self.player_index +=1
        #     print(self.player_index)
        #     self.direction = pygame.math.Vector2()

    def get_status(self):

        if self.direction.magnitude() == 0:
            # self.status +=self.status.split('_')[0] + "idle"
            self.status += '_idle'

        if self.timers[USE_ATTACK].active:
            Shoot(self,self.group,self.collision_sprites)
            print("shoot line")
  
        # if self.timers[player_turn].active:
            # print("player turn: " + str(self.timers[player_turn].active))
    
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

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
            # elif hasattr(sprite,'attackbox'):
            #     if sprite.attackbox.colliderect(self.attackbox):
            #         # print('attack box')
                    # add attack phase here 

    def move(self,dt):
    
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.attackbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.attackbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')
      
    def update(self,dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(dt)
        # self.animate(dt)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,player,group):
        super().__init__(group)

        self.enemy_type = ENEMY_1
        self.import_assets()
        self.status = '_idle'
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']
      
        self.player = player
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 75

        # self.hitbox = self.rect.copy()
        self.attackbox = self.rect.copy()
        self.enemyHitbox = self.rect.copy()
        

    def import_assets(self):
        self.animations = {'_idle':[],'left_idle':[],'left':[],'right_idle':[],'right':[]}
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
        
        # if self.timers[use_attack].active:
        #     print("attack is be used")
        
        # if self.timers[player_turn].active:
            # print("player turn: " + str(self.timers[player_turn].active))


    def move(self,dt):

        self.direction.x, self.direction.y = self.player.rect.x - self.rect.x, self.player.rect.y - self.rect.y
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #horizontal movement
        if self.rect.x > self.player.rect.x:
            self.status = LEFT
        self.pos.x += self.direction.x * self.speed * dt
        self.attackbox.centerx = round(self.pos.x)
        self.enemyHitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.attackbox.centerx
        
        #vertical movement
        if self.rect.x < self.player.rect.x:
            self.status = RIGHT
        self.pos.y += self.direction.y * self.speed * dt
        self.attackbox.centery = round(self.pos.y)
        self.enemyHitbox.centery = round(self.pos.y)
        self.rect.centery = self.attackbox.centery
        

    def update(self,dt):
        self.get_status()
        self.move(dt)
        self.animate(dt)


class Spawn:
    def __init__(self,player,group):
        self.player = player
        self.group = group
        self.setup()


    def setup(self):
        side = ['top','bottom','left','right']
        
        for i in range(random.randrange(4,15)):            
            choice1 = random.choice(side)
            choice2 = random.choice(side)
            # print(SPAWN_LOCATION[choice1],SPAWN_LOCATION[choice2])
            Enemy((SPAWN_LOCATION[choice1],SPAWN_LOCATION[choice2]),self.player,self.group)
            
         

        