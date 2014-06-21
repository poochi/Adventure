"""
Thanks to 
Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe
Pygame

"""

import pygame

import constants
import levels

from player import Player

def main():
    """ Main Program """
    # setup mixer to avoid sound lag
    pygame.mixer.pre_init(44100, -16, 2, 2048) 
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption(constants.TITLE)
    
    pygame.mixer.init();

    pygame.mixer.music.load(constants.BGM)
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play(-1)
    try:
        sound  = pygame.mixer.Sound(constants.JUMP_1);
    except:
        raise UserWarning, "could not load or play soundfiles in folder :-("
        return;
    
    
    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    player_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height ;
    player_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        
        for event in pygame.event.get():
            # On close
            if event.type == pygame.QUIT: 
                done = True 
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                    sound.stop();
                    sound.play();
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        player_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)
            
        current_level.draw(screen)
        player_sprite_list.draw(screen)        
        
        clock.tick(constants.FPS)

        # Update only modified rectangle regions
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
