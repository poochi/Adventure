""" Module implementing Enemies """

import constants
import pygame
from spritesheet_functions import SpriteSheet
import math

FLY1 = (0,32,72,36);
FLY2 = (0,0,75,31);
class Enemies(pygame.sprite.Sprite):
    sprite_sheet = None;
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = SpriteSheet(constants.ENEMIES)
        
        
        
        


class Rock(Enemies):
    change_x = 0;
    change_y  = 0;
    frame = 0;
    image_list = [];
    
    def __init__(self,initvalues):
        
        try:
            
            x = int(initvalues['posx']);
            y = int(initvalues['posy']);
        except:
            print "position not spec returning None";
            return None;
        Enemies.__init__(self);
        self.image_list.append(self.sprite_sheet.get_image(FLY1[0],FLY1[1],FLY1[2],FLY1[3]));
        self.image_list.append(self.sprite_sheet.get_image(FLY2[0],FLY2[1],FLY2[2],FLY2[3]));
        self.image = self.image_list[0]
        self.rect = self.image.get_rect();
        self.rect.x = x;
        self.rect.y = y;
        

    def update(self):
        self.rect.x+=self.change_x;
        self.rect.y+=self.change_y;
        self.frame +=1;
        self.image = self.image_list[0];
        self.change_x = (self.frame%10 - 5);
        self.change_y = 0;
        
        


    
        
        
