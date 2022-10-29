from pygame import Vector2

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
TILE_SIZE = 64
WINDOW_WIDTH = 950
WINDOW_HEIGHT = 580

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
# ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
FONT_SIZE = 18
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR_ACTIVE = 'gold'


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
    'health bar' : "healthbar",
    'sketch':'sketch_board'
}

PATHS = {
    'player base' : '../resources/character/',
    'enemy base' : '../resources/enemy/',
    'overlay path' : '../resources/assets/',
    'data path' : '../resources/data/tmx/map.tmx'
}


OVERLAY_POSITIONS = {
    'health bar' :(SCREEN_WIDTH - 125,25),
    'progress bar' :(70, SCREEN_HEIGHT -5),
    'sketch' : (10,5)
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

SPAWN_LOCATION ={
    'top' : -180,
    'bottom': WINDOW_HEIGHT + 180,
    'left': -180,
    'right': WINDOW_WIDTH + 180
}

FONT = 'comicsansms'
FONT_SIZE = {
    'small' : 25,
    'medium' : 50,
    'large': 85
}

PLAYER_HOOT_OFFSET = {
    'left':Vector2(-50,0), # 40
    'right':Vector2(50,0), # 40
    'up': Vector2(0,-50),
    'down':Vector2(0,50)
}

PLAYER_WING_OFFSET = {
    'left': Vector2(-100,0),
    'right': Vector2(100,0),
    'up': Vector2(0,-100),
    'down': Vector2(0,100)


}

