# Color
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
# E
# E
ENTITY_SHOT_DELAY = {
    'player1': 5,
    'player2': 3,
    'Enemy1': 80,
    'Enemy2': 150,
    'Enemy3': 130
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 2,
    'Level3Bg3': 3,
    'Level3Bg4': 4,
    'Level3Bg5': 5,
    'player1': 5,
    'player2': 5,
    'player1Shot': 4,
    'player2Shot': 3,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy1Shot': 4,
    'Enemy2Shot': 2,
    'Enemy3Shot': 6,
}
ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2':0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level3Bg5': 0,
    'player1': 1,
    'player1Shot': 25,
    'player2': 1,
    'player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
    'Enemy3': 3,
    'Enemy3Shot': 30,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level3Bg5': 0,
    'player1': 0,
    'player1Shot': 0,
    'player2': 0,
    'player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Enemy3': 130,
    'Enemy3Shot': 0,

}
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Level3Bg4': 999,
    'Level3Bg5': 999,
    'player1': 150,
    'player2': 150,
    'player1Shot': 1,
    'player2Shot': 1,
    'Enemy1': 100,
    'Enemy1Shot': 1,
    'Enemy2': 90,
    'Enemy2Shot': 1,
    'Enemy3': 120,
    'Enemy3Shot': 1

}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
#
NAME_RU = 'Talita Ferreira - 4709280'
# P
PLAYER_KEY_UP = {'player1': pygame.K_UP,
                 'player2': pygame.K_w}
PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN,
                   'player2': pygame.K_s}
PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT,
                   'player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT,
                    'player2': pygame.K_d}

PLAYER_KEY_SHOOT = {'player1': pygame.K_RCTRL,
                    'player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 1000 #criar inimgos na tela 4s



# T
TIMEOUT_STEP = 100 #100 MILI S
TIMEOUT_LEVEL = 20000 # 20 SEG
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

#s
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
# V
