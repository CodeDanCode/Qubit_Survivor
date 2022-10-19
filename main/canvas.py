import pygame
from support import *
from settings import *

class Canvas:
    def __init__(self,player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        # self.import_assets()

    # def import_assets(self):
    #     self.assets = {'background':[],'control_panel':[],'logo':[],'sketch':[]}
    #     for asset in self.assets.keys():
    #         full_path = '../resources/assets'
    #         self.assets[asset] = import_folder(full_path)
    #         print(self.assets)
