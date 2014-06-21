""" Score Board , Life and other embellishement representations English """

import pygame
import constants
from spritesheet_functions import SpriteSheet


#x="230" y="0" width="30" height="38"

class Stats(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite_sheet = SpriteSheet(constants.NUMBERS_SHEET)
        self.numberimages=[];

        self.numberimages.append(self.sprite_sheet.get_image(230,0,30,38));
        self.numberimages.append(self.sprite_sheet.get_image(196,41,26,37));
        self.numberimages.append(self.sprite_sheet.get_image(55,98,32,38));
        self.numberimages.append(self.sprite_sheet.get_image(239,80,28,38));
        self.numberimages.append(self.sprite_sheet.get_image(239,122,29,38));
        self.numberimages.append(self.sprite_sheet.get_image(238,162,28,38));
        self.numberimages.append(self.sprite_sheet.get_image(230,40,30,38));
        self.numberimages.append(self.sprite_sheet.get_image(226,206,32,39));
        self.numberimages.append(self.sprite_sheet.get_image(192,206,32,40));
        self.numberimages.append(self.sprite_sheet.get_image(196,0,32,39));
        self.image = None;
    def getImage(self,score):
        
        assert(len(str(score))==1);
        assert(score in range(10));
        return self.numberimages[score];
            
        
        

