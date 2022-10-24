import pygame
from settings import *

class Shoot(pygame.sprite.Sprite):
    def __init__(self,player,group,collision_group):
        super().__init__(group)
        self.player = player
        self.collision_group = collision_group

        self.image = pygame.Surface((50,10))
        self.image.fill(COLORS['blue']) 
        # self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = (self.player.pos.x,self.player.pos.y))
        self.z = LAYERS['main']
        # self.particlehitbox = self.rect.copy()

    def attack_collide(self,direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite.enemyHitbox):
                if sprite.enemyHitbox.colliderect(self.particlehitbox):
                    if direction == 'horizontal':
                        print("hit enemy")

    # def move(self):
    #     if self.player.pos.x

    def update(self,dt):
        self.rect.x += 5