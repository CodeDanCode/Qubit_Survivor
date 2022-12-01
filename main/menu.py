import pygame
from level import *
from support import *


class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.level = Level()
        self.selected = None



    def intro(self):
        self.display_surface.fill(pygame.Color('White'))


        message_to_screen(
                self.display_surface,
                'Controls', 
                COLORS['black'],
                TEXT_POS['title'],
                FONT_SIZE['medium']
                )


        # easy button
        self.button(
            'eazy',
            TEXT_POS['button_1'],
            COLORS['blue'],
            COLORS['red'],
            'easy'
            )
        # medium button
        self.button(
            'normal',
            TEXT_POS['button_2'],
            COLORS['blue'],
            COLORS['red'],
            'normal'
            )
        # hard button
        self.button(
            'hard',
            TEXT_POS['button_3'],
            COLORS['blue'],
            COLORS['red'],
            'hard'
            )



    def button(self,text,pos, inactive_color, active_color, action = None):
         cur = pygame.mouse.get_pos()
         click = pygame.mouse.get_pressed()

         if pos[0] + BUTTON_SIZE[0] > cur[0] > pos[0] and pos[1] + BUTTON_SIZE[1] > cur[1] > pos[1]:
             
             pygame.draw.rect(self.display_surface, active_color,(pos[0],pos[1],BUTTON_SIZE[0],BUTTON_SIZE[1]))
             
             if click [0] == 1 and action != None:
                if action == "easy":
                    self.selected = 'easy'
                if action == "normal":
                    self.selected = 'normal'
                if action == "hard":
                    self.selected = 'hard'
                    
         else:
             pygame.draw.rect(self.display_surface, inactive_color,(pos[0],pos[1],BUTTON_SIZE[0],BUTTON_SIZE[1]))

         text_to_button(self.display_surface,text,COLORS['black'],pos)
         
    def run(self,dt):

        if self.selected != None:
            self.level.run(dt,self.selected)
        else:
            self.intro()

        
        