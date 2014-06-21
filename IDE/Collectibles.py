"""
Module for managing
Collectibles like coins  """
import pygame
import constants
from spritesheet_functions import SpriteSheet


#GOLD = "GOLD"

VALUE = {'BRONZE':10,'GOLD':30,'SILVER':30};
GOLD_COIN = (0,0,35,35);
class Collectibles(pygame.sprite.Sprite):
    def __init__(self):
        return;


class Coins(Collectibles):
    
    image = None;
    
    
    def __init__(self,initvalues):
        pygame.sprite.Sprite.__init__(self);
        
        try :
            color = initvalues['name'];
            x = int(initvalues['posx']);
            y = int(initvalues['posy']);
        except:
            color = 'GOLD';
        assert(color in VALUE.keys());
        self.color = color;
        self.value = VALUE[color];
        sprite_sheet = SpriteSheet(constants.GOLD_COIN_SHEET)
        # Grab the image for this platform
        self.coins=[];
        self.image = sprite_sheet.get_image(GOLD_COIN[0], GOLD_COIN[1], GOLD_COIN[2], GOLD_COIN[3])
       
        self.rect = self.image.get_rect();
        self.rect.x = x;
        self.rect.y = y;

   
    
      
    
        
        
        

    
        
    
