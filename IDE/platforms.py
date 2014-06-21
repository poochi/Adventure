"""
Module for managing platforms.
"""
import pygame

from spritesheet_functions import SpriteSheet
import constants;
import Stats;

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

GRASS_LEFT            = (576, 720, 70, 70)
GRASS_RIGHT           = (576, 576, 70, 70)
GRASS_MIDDLE          = (504, 576, 70, 70)
STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, initvalues):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        try :
            name = initvalues['name'];
            x = int(initvalues['posx']);
            y = int(initvalues['posy']);
            
        except:
            print "Type of platform not determinable";
            return ;
        
        pygame.sprite.Sprite.__init__(self)
        if name == 'GRASS_LEFT':
            sprite_sheet_data = GRASS_LEFT;
        if name == 'GRASS_RIGHT':
            sprite_sheet_data = GRASS_RIGHT;
        if name == 'GRASS_MIDDLE':
            sprite_sheet_data = GRASS_MIDDLE;
        if name == 'STONE_PLATFORM_LEFT':
            sprite_sheet_data = STONE_PLATFORM_LEFT;
            
        if name == 'STONE_PLATFORM_MIDDLE':
            sprite_sheet_data = STONE_PLATFORM_MIDDLE;
            
        if name == 'STONE_PLATFORM_RIGHT':
            sprite_sheet_data = STONE_PLATFORM_RIGHT;
        
        
        assert(sprite_sheet_data is not None);
        sprite_sheet = SpriteSheet(constants.TILE_SHEET)
        
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect();
        self.rect.x =x;
        self.rect.y = y;


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def __init__(self,initvalues):
        Platform.__init__(self,initvalues);
        try :
            self.change_x = initvalues['change_x'];
            self.boundaryleft = initvalues['boundaryleft'];
            self.boundaryright = initvalues['boundaryright'];
            
        except:
            print "assigning Default values Movingplatform";
            self.change_x = 1;
            
                

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
