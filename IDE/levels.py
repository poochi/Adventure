import pygame


#INIT for any leaf object is through dictionaries only

import constants
import platforms
import FlyingObjects
import Collectibles
import Stats;
import Enemies;
import Background;
import loadable

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.flying_object_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.collectibles_list = pygame.sprite.Group()
        self.player = player
        self.scoreboard = Stats.Stats();
        self.repeatcount = 0;
        

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        """Remove unwanted objects """
        self.platform_list.update();
        self.enemy_list.update();      
        self.flying_object_list.update();
        self.collectibles_list.update();
        #Removing unwanted objects
        
        for eachcoin in self.collectibles_list:
            hit = pygame.sprite.collide_rect(eachcoin, self.player)
            if hit:
                self.player.score+= eachcoin.value;
                self.collectibles_list.remove(eachcoin);
                
            
        
              
                
        

    def draw(self, screen):
        """ Draw everything on this level. """        

        # Draw the background
        #The background class takes care of giving us background images .
        
        screen.fill(constants.BLUE)
        for eachimg,eachpos in self.background.get_screenobjs(self.world_shift):
            screen.blit(eachimg,(eachpos,0));
        
        
        font = pygame.font.Font(None, 36)
        text = font.render("SCORE: ", 1, (10, 10, 10))
        textpos = [constants.SCREEN_WIDTH-constants.SCORE_WIDTH,constants.SCORE_HEIGHT]
        screen.blit(text,textpos);
        wd = 120;
        textpos[0]+=wd
        for each in str(self.player.score):
            img = self.scoreboard.getImage(int(each));
            screen.blit(img,(textpos[0],textpos[1]));
            textpos[0]+=img.get_rect().width
            

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.flying_object_list.draw(screen);
        self.collectibles_list.draw(screen);

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for objs in self.flying_object_list:
            objs.rect.x += shift_x

        for objs in self.collectibles_list:
            objs.rect.x += shift_x
            

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        ### READ FROM THE XML FILE AND GENERATE THE WORLD
        print loadable.BACKGOUND_PATH_LIST[0]
        self.background = Background.Background(loadable.BACKGOUND_PATH_LIST[0]);
        
        
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.

        Immovableplatforms = loadable.Immovableplatforms;
        Movableplatforms = loadable.Movableplatforms;
        
        flyingObjects = loadable.FlyingObject;
        coins = loadable.collectible;


        Rocks = loadable.Rocks;
        
        for each in Rocks:
            print int(each['posy'])
            
            block = FlyingObjects.Bats(each);
            print type(block)
            
            self.enemy_list.add(block);

        for each in flyingObjects :
            
            block = FlyingObjects.Helicopter(each);
            block.change_x = 3;
            block.level = self;
            self.flying_object_list.add(block)
            

        for each in coins:
            block = Collectibles.Coins(each);
            
            block.level = self;
            self.collectibles_list.add(block)
            
            


        # Go through the array above and add platforms
        for platform in Immovableplatforms:
            block = platforms.Platform(platform)
            
            self.platform_list.add(block)
        
            

        #Movable platforms  
        for plaform in Movableplatforms:
            block = platforms.MovingPlatform(plaform)
            block.rect.x = 1350
            block.rect.y = 280
            block.boundary_left = 1350
            block.boundary_right = 1600
            block.change_x = 1
            block.player = self.player
            block.level = self
            self.platform_list.add(block)


