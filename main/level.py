import pygame
from settings import *
from player import *
from overlay import *
from sprites import *
from pytmx.util_pygame import load_pygame
import random
from enemy import *
from timers import Timer


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.setup()
        self.overlay = Overlay(self.player)
        self.timers = {
            'spawn' : Timer(5000,self.enemy.randomSpawn)
        }

    def setup(self):
        tmx_data = load_pygame(PATHS['data path'])
        
        # Map collision 
        for x,y,surf in tmx_data.get_layer_by_name('collision').tiles():
            Generic((x*TILE_SIZE,y*TILE_SIZE), pygame.Surface((TILE_SIZE,TILE_SIZE)), self.collision_sprites)

        # Player Location Object
        for obj in tmx_data.get_layer_by_name('Player'):
            if obj.name == 'start':
                self.player = Player((obj.x,obj.y),self.all_sprites,self.collision_sprites,self.enemy_sprites)
        
        Generic(
            pos = (0,0),
            surf = pygame.image.load('../resources/assets/map.png').convert_alpha(), # change to settings variable here 
            groups = self.all_sprites,
            z = LAYERS['ground']
        )

        self.enemy = Spawn(self.player,[self.all_sprites,self.collision_sprites,self.enemy_sprites])
        # self.enemy = Enemy((SPAWN_LOCATION['top'],SPAWN_LOCATION['top']),self.player,[self.all_sprites,self.collision_sprites,self.enemy_sprites])

    def update_timers(self):
        if not self.timers['spawn'].active:
            self.timers['spawn'].activate()

        for timer in self.timers.values():
            timer.update()

    def run(self, dt,selected):

        self.display_surface.fill(COLORS['blue'])
        if not self.player.game_over:
            self.all_sprites.custom_draw(self.player,self.enemy)
    
            self.all_sprites.update(dt,selected)
            self.overlay.display()
        else:
            self.display_surface.fill(COLORS['white'])
            self.game_over()

    def game_over(self):

        message_to_screen(
            self.display_surface,
            'Game Over', 
            COLORS['black'],
            TEXT_POS['title'],
            FONT_SIZE['medium']
            )

        self.button(
            'Play Again',
            TEXT_POS['button_2'],
            COLORS['blue'],
            COLORS['red'],
            'restart'
            )


    def button(self,text,pos,inactive_color,active_color,action = None):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if pos[0] + BUTTON_SIZE[0] > cur[0] > pos[0] and pos[1] + BUTTON_SIZE[1] > cur[1] > pos[1]:
             
            pygame.draw.rect(self.display_surface, active_color,(pos[0],pos[1],BUTTON_SIZE[0],BUTTON_SIZE[1]))
             
            if click [0] == 1 and action != None:
                if action == "restart":
                    pass
                    
        else:
            pygame.draw.rect(self.display_surface, inactive_color,(pos[0],pos[1],BUTTON_SIZE[0],BUTTON_SIZE[1]))

        text_to_button(self.display_surface,text,COLORS['black'],pos)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.custom_surface = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.offset = pygame.math.Vector2()


    def custom_draw(self, player,enemy):
        self.offset.x = (player.rect.centerx - WINDOW_WIDTH/2)
        self.offset.y = (player.rect.centery - WINDOW_HEIGHT/2)

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    
                   
                    if sprite == player:

                       
                        attackbox_rect = player.attackbox.copy()
                        attackbox_rect.center = offset_rect.center
                        pygame.draw.rect(self.custom_surface,COLORS['blue'],attackbox_rect,5)

                        hitbox_rect = player.hitbox.copy()
                        hitbox_rect.center = offset_rect.center
                        pygame.draw.rect(self.custom_surface,COLORS['green'],hitbox_rect,5)
                        
                        enemy_rect = player.enemybox.copy()
                        enemy_rect.center = offset_rect.center
                        pygame.draw.rect(self.custom_surface,'orange',enemy_rect,5)


                        target_hoot_pos = offset_rect.center + PLAYER_HOOT_OFFSET[player.status.split('_')[0]]
                        pygame.draw.circle(self.custom_surface,'blue',target_hoot_pos,5)
                        
                        target_wing_pos = offset_rect.center + PLAYER_WING_OFFSET[player.status.split('_')[0]]
                        pygame.draw.circle(self.custom_surface,'purple',target_wing_pos,5)




                    # if sprite == enemy:
                    #     pygame.draw.circle(self.custom_surface,'yellow',offset_rect.center,5)
                    #     attackbox_rect = enemy.attackbox.copy()
                    #     attackbox_rect.center = offset_rect.center
                    #     pygame.draw.rect(self.custom_surface,COLORS['blue'],attackbox_rect,5)
                    #     hitbox_rect = enemy.hitbox.copy()
                    #     hitbox_rect.center = offset_rect.center
                    #     pygame.draw.rect(self.custom_surface,COLORS['green'],hitbox_rect,5)

                    self.custom_surface.blit(sprite.image,offset_rect)
                    self.display_surface.blit(self.custom_surface,(240,5))

class Spawn:
    def __init__(self,player,group):
        self.player = player
        self.group = group
        self.randomSpawn()


    def randomSpawn(self):
        side = ['top','bottom','left','right']

        for i in range(random.randrange(4,15)):            
            choice1 = random.choice(side)
            choice2 = random.choice(side)
            self.enemy = Enemy((SPAWN_LOCATION[choice1],SPAWN_LOCATION[choice2]),self.player,self.group,ENEMY_1)
        return self.enemy
         