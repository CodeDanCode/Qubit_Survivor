import pygame
from settings import *
from support import *
from timer import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group,collision_sprites):
        super().__init__(group)
        # Will use this for import character assets 
        self.import_assets()
        self.status = '_idle'
        self.frame_index = 0 

        # general sprite setup  
        self.image = pygame.Surface((32,64)) # remove temp surface 
        self.image.fill(GREEN) # remove surface fill
        # self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        # character movement variables
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
        self.timers = {
            USE_ATTACK: Timer(350, self.use_attack),
            PLAYER_TURN: Timer(200)
            }

        self.selected_attack = 'hoot'

        # for collision of sprite boxes
        self.attack_box = self.rect.copy().inflate(self.rect.width * 0.3, self.rect.height * 0.3)
        self.collision_sprites = collision_sprites

    def import_assets(self):
        self.animations = {'_idle':[],'up':[],'down':[],'left':[],'right':[],
                            'left_attack':[],'right_attack':[]}

        for animation in self.animations.keys():
            full_path = "../resources/character/" + animation
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
            print("attack is be used")
        
        # if self.timers[player_turn].active:
            # print("player turn: " + str(self.timers[player_turn].active))
    


    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def move(self,dt):
    
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.attack_box.centerx = round(self.pos.x)
        self.rect.centerx = self.attack_box.centerx
        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.attack_box.centery = round(self.pos.y)
        self.rect.centery = self.attack_box.centery
      

    def update(self,dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(dt)
        # self.animate(dt)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,player,group):
        super().__init__(group)

        self.enemy_type = 'robot'
        self.import_assets()
        self.status = '_idle'
        self.frame_index = 0

        # self.image = pygame.Surface((24,24))    
        # self.circle = pygame.draw.circle(self.image,RED,(12,12),12)
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
      
        self.player = player
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 75
        

    def import_assets(self):
        self.animations = {'_idle':[],'left_idle':[],'left':[],'right_idle':[],'right':[]}
        for animation in self.animations.keys():
            full_path = "../resources/enemy/"+ self.enemy_type +"/"+ animation
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
            self.status = 'left'
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        
        #vertical movement
        if self.rect.x < self.player.rect.x:
            self.status = 'right'
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        

    def update(self,dt):
        self.get_status()
        self.move(dt)
        self.animate(dt)