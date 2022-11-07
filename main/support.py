import pygame
from os import walk
from settings import *


def import_folder(path):
    surface_list = []

    for __,__, img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf,(32,32)) # change sprite size in support
            surface_list.append(image_surf)

    return surface_list



def text_objects(text, color,size):
    font = pygame.font.SysFont(FONT, size)
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def message_to_screen(surf,msg,color, pos, size = FONT_SIZE['small']):
    textSurf, textRect = text_objects(msg,color,size)    
    textRect.center = pos  
    surf.blit(textSurf, textRect)

def text_to_button(surf,msg,color,pos,size = FONT_SIZE['small']):    
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = (pos[0]+(BUTTON_SIZE[0]/2), pos[1]+(BUTTON_SIZE[1]/2))   
    surf.blit(textSurf, textRect)

