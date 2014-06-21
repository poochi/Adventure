"""
Global constants
"""

import os
current_dir = os.getcwd();


# Colors
BLACK    = (   0,   0,   0) 
WHITE    = ( 255, 255, 255) 
BLUE     = (   0,   0, 255)



# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

TILE_SHEET =  os.path.join(os.getcwd(),"..","Assets","tiles_spritesheet.png");
PLAYER = os.path.join(os.getcwd(),"..","Assets","p1_walk.png")
TITLE = "LuLu s Adventure"
BGM = os.path.join(os.getcwd(),"..","Assets","StockSoundsV3cutVersion.wav");
#BEEP = "beep.ogg"
JUMP_1 = os.path.join(os.getcwd(),"..","Assets","jump_01.wav")
#JUMP_1 = "Alarm.wav"
HELICOPTER_SHEET = os.path.join(os.getcwd(),"..","Assets","planes.png")
GOLD_COIN_SHEET = os.path.join(os.getcwd(),"..","Assets","coin_gold.png")
ROCK_SHEET = os.path.join(os.getcwd(),"..","Assets","dirtCaveRockSmall.png")
BAT_SHEET = os.path.join(os.getcwd(),"..","Assets","bat.png")
NUMBERS_SHEET = os.path.join(os.getcwd(),"..","Assets","hud_spritesheet.png")
ENEMIES = os.path.join(os.getcwd(),"..","Assets","enemies_spritesheet.png")
BCK_LEVEL1 = os.path.join(os.getcwd(),"..","Assets","background_01.png")
BCK_OVERLAP = 0
SCORE_WIDTH = 300
SCORE_HEIGHT = 20
FPS = 60

