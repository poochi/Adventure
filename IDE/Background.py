#New Background class
import pygame;
import constants;
from ast import literal_eval;
import os

#Assumes path is Relative to Asset folder .

class Background():
    def __init__(self,initvalues):
        try :
            print initvalues['path'];
            path = literal_eval(initvalues['path']);
            
            assert(type(path)is list);
        except(KeyError):
            print "Check Config File GAMECONFIG.xml "+Background.__name__+ " does not contain path (list) key !!"
            return;
        
        
        #self.ImageAstart = 0;
        #self.ImageBend = 0;
        self.img =[];
        #self.imgAind = 0
        #self.imgBind = 0

        
        
        for each in path:
            self.img.append(pygame.image.load(os.path.join(os.getcwd(),'..','Assets',each)).convert());
        self.img[0].set_colorkey(constants.BLUE)
        
    
    def fill_imageind(self, previous):
       self.preind = 0;
       self.curind = 0;
       self.nextind = 0;
       return 0;
        
        
    def get_screenobjs(self, worldshift):
        #Always place 3 images .
        # v/wd index of image v%wd loc of image
        
        self.fill_imageind(worldshift)
        
        
        v = abs(worldshift)%self.img[0].get_rect().width;
        v = v if worldshift >0 else -v;
        
        return [[self.img[self.preind], v-self.img[self.preind].get_rect().width], [self.img[self.curind], v],[ 
        self.img[self.nextind], v+self.img[self.curind].get_rect().width]]

