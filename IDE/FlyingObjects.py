"""
Module for managing
moving object  """

import pygame

from spritesheet_functions import SpriteSheet
import constants;


	
BLUE_PLANE_SPRITE_DATA = [
(0, 73, 88, 73),
 (0, 0, 88, 73),
 (0, 65, 88, 73)]

BAT_SPRITE_DATA = (0,0,70,47);

class FlyingObjects(pygame.sprite.Sprite):
    def __init__():
        return;
    

    
class Helicopter(FlyingObjects):
    """ Helicopters in AIR """
    change_x = 0;
    change_y = 0;
    image = None;
    level = None;
    
    def __init__(self,initvalues):
        pygame.sprite.Sprite.__init__(self)
        color = "BLUE"
        try :
            
            #color = initvalues['color'];
            x = int(initvalues['posx']);
            y = int(initvalues['posy']);
        except:
            color="BLUE"
            print "Violations"
            return;
            
        self.color = color;
        sprite_sheet = SpriteSheet(constants.HELICOPTER_SHEET)
        # Grab the image for this platform
        self.helicopter_frame_list=[];

        # Specific to the sprite set
        for each_sprite_sheet_data in BLUE_PLANE_SPRITE_DATA:
            img = sprite_sheet.get_image(each_sprite_sheet_data[0], each_sprite_sheet_data[1], each_sprite_sheet_data[2], each_sprite_sheet_data[3])
            self.helicopter_frame_list.append(img);

        self.image = self.helicopter_frame_list[0];
        self.rect = self.image.get_rect();
        
        self.rect.x = x;
        self.rect.y = y;
        

    def update(self):
        
        self.rect.x+=self.change_x;
        self.rect.y+=self.change_y;
        
        self.image = self.helicopter_frame_list[(self.rect.x//30)%len(self.helicopter_frame_list)];
        #self.rect.x +=self.level.world_shift;
        

        #To do Collison.
class Bats(FlyingObjects):
    nature = "ENEMY";
    change_x = 3;
    change_y = 2;
    cnt = 0;
    
    def __init__(self,initvalues):
        
        try :
            
            x = int(initvalues['posx']);
            y = int(initvalues['posy']);
            
        except:
            print "------------------------Missing/incorrect DATA----------------------------";
            return;
        
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet(constants.BAT_SHEET);
        self.image = sprite_sheet.get_image(BAT_SPRITE_DATA[0], BAT_SPRITE_DATA[1], BAT_SPRITE_DATA[2], BAT_SPRITE_DATA[3]);
        assert(self.image is not None);
        self.rect = self.image.get_rect();
        self.rect.x = x;
        self.rect.y = y;
    def update(self):
        self.cnt+=1;
        """Random init call """
        if self.cnt >= 300 :
            self.rect.x+=self.change_x;
            self.rect.y+=self.change_y;
            self.change_y+= 3;
            
        
        
        
        
    
        
        
    
    
