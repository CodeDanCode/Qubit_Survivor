from pygame import Vector2

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
TILE_SIZE = 64


RUN = True
NUM_ENEMIES = None
PLAYER_TURN = 'player turn'
USE_ATTACK = 'use attack'

# control direction
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# enemies
ENEMY_1 = 'zombie'
ENEMY_2 = 'robot'
ENEMY_BOSS_1 = 'boss_zombie'
ENEMY_BOSS_2 = 'boss_robot'

OVERLAYS ={
    'health bar' : "healthbar"
}

PATHS = {
    'player base' : '../resources/character/',
    'enemy base' : '../resources/enemy/',
    'overlay path' : '../resources/assets/'
}


OVERLAY_POSITIONS = {
    'health bar' :(SCREEN_WIDTH - 125,50),
    'progress bar' :(70, SCREEN_HEIGHT -5)
}

COLORS = {
    'red' : (255, 0, 0),
    'green':(0,255,0),
    'blue' : (0,0,255),
    'black' : (0,0,0),
    'white' : (255,255,255)
}

LAYERS = {
    'ground':0,
    'main':1,
    'items':2
}

