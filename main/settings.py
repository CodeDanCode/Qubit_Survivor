from pygame import Vector2

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
TILE_SIZE = 64
WINDOW_WIDTH = 950
WINDOW_HEIGHT = 580

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ITEM_BOX_SIZE = 80

FONT = 'comicsansms'
FONT_SIZE = {
    'xsmall': 16,
    'small' : 25,
    'medium' : 50,
    'large': 85
}

BUTTON_SIZE =  (150,70)

TEXT_POS = {
    'title': (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) - 150),
    'button_1': (225,450),
    'button_2': (525,450),
    'button_3': (825,450),
    'refresh': (int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2))
    
}


TEXT_COLOR = '#EEEEEE'
HEALTH_COLOR = 'red'

UI_BG_COLOR = '#222222'
UI_BORDER_COLOR ='#111111'
UI_BORDER_COLOR_ACTIVE = 'gold'


# control direction
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# enemies
ENEMY_1 = 'zombie'
ENEMY_2 = 'robot'
ENEMY_BOSS_1 = 'zombie boss'
ENEMY_BOSS_2 = 'robot boss'

OVERLAYS ={
    'health bar' : "healthbar",
    'sketch':'sketch_board',
    'test': 'test',
    'control_bar':'control_bar'
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
    'sketch' : (10,5),
    'control': (10,410)
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
    'items':2,
    'overlay':3
}

SPAWN_LOCATION ={
    'top' : -180,
    'bottom': WINDOW_HEIGHT + 180,
    'left': -180,
    'right': WINDOW_WIDTH + 180
}


PLAYER_HOOT_OFFSET = {
    'left':Vector2(-80,0), # 40
    'right':Vector2(80,0), # 40
    'up': Vector2(0,-80),
    'down':Vector2(0,80)
}

PLAYER_WING_OFFSET = {
    'left': Vector2(-165,0),
    'right': Vector2(165,0),
    'up': Vector2(0,-165),
    'down': Vector2(0,165)
}

weapon_data = {
    'hoot' : {'cooldown': 100, 'damage': 15, 'graphic': '../resources/assets/hoot.png'},
    'wing' : {'cooldown': 400, 'damage' : 30, 'graphic': '../resources/assets/wing.png'}
}


ENEMY_DATA= {
    'zombie' : {'health':25,'speed':70,'damage':25,'exp':100, 'attack_sound':'../resources/sounds/zombie_hit.mp3'},
    'zombie boss': {'health': 100, 'speed':50, 'damage': 50,'exp':200, 'attack_sound':'../resources/sounds/zombie_hit.mp3'},
    'robot' : {'health':30, 'speed': 80, 'damage': 35,'exp':140, 'attack_sound':'../resources/sounds/robot_hit.mp3'},
    'robot boss' : {'health': 120, 'speed': 60, 'damage':60,'exp':240, 'attack_sound':'../resources/sounds/robot_hit.mp3'}
}

qstate_data = {
    'H': '../resources/qstates/H.png',
    'I': '../resources/qstates/I.png',
    'S': '../resources/qstates/S.png',
    'T': '../resources/qstates/T.png',
    'X': '../resources/qstates/X.png',
    'Y': '../resources/qstates/Y.png',
    'Z': '../resources/qstates/Z.png'
}

CONTROL_BOX = {
    0: (50,440), #add placement for images on control line
    1: (50,490),
    2: (50,530),
}

