"""*
    TO DO : 
        - Appliquer PEP8
        - Modifier Item Seringue (en cours)
        - Ajout des commentaires de classe
        - Corriger Item.TYPE (OK)
        - Corriger Special Slot
        - Ajouter Aspect Graphique Victoire/Défaite
        - Voir si Enum est utilisable dans les autres classes
"""
import pygame
import random

from pygame.locals import *
from constants import *
from character import *
from item import *
from level import *
from ui import *

def create_item(item_type):
    item = Item(item_type, level)
    item.create()

def display_text(window, str_text, color, size, px = int(SCREEN_WIDTH/2), py=int(SCREEN_HEIGHT/2), font=None):
    font = pygame.font.Font(font, size)
    text = font.render(str_text, 1, color)
    text_rect = text.get_rect(center=(px, py))
    window.blit(text, text_rect)

def check_victory():
    if not player.is_weak and player.position == guard.position:
        player_win = True
        print('*************')
        print('The guard has been asleep, you escaped from the maze')
        print('Congratulation, YOU WIN !!')
        print('*************')
        display_text(main_window, "Congratulations !!! YOU WIN !!!", (255,204,0), 40)    
        return True
    elif player.is_weak and player.position == guard.position:
        player_win = False
        print('*************')
        print('The guard killed you')
        print('You lose ...')
        print('*************')
        display_text(main_window, "YOU LOSE !!!", (255,0,0), 40)
        return True
    

pygame.init()

# Pygame Main Window
main_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Pygame Main Window Custom
pygame.display.set_caption(TITLE_WINDOW)


# Main Loop (Game Loop)
game_window = True
while game_window:
    print('Loading...')
    # Init. Item list
    Item.instances_in_level = []
    # Create level structure
    level = Level(LVL_LABYRINTH)
    level.gen_level(main_window)
    # Create Player
    player = Player(sprite_player, level, level.begin_position)
    player_win = False
    # UI
    ui = UI(player, main_window)
    # Create Guardian
    guard = Guardian(sprite_guard, level, level.end_position)
    # Items Creation
    create_item(Type.TUBE)
    create_item(Type.PRODUIT)
    create_item(Type.AIGUILLE)

    print('Nb items in Level : ' + str(len(Item.instances_in_level)))
    print('...Ready')
    
    end_pause = False
    game_loop = True
    while game_loop:
        level.gen_level(main_window)
        ui.draw()
        
        for item in Item.instances_in_level:
            main_window.blit(item.sprite, (item.position))
        main_window.blit(guard.sprite, (guard.x, guard.y))
        main_window.blit(player.sprite, (player.x, player.y))

        for event in pygame.event.get():
            # If player want to quit the game, game_loop = False
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                game_loop = False
                game_window = False

            if event.type == KEYDOWN:
                if event.key == K_RIGHT: player.move('right')
                if event.key == K_LEFT: player.move('left')
                if event.key == K_UP: player.move('up')
                if event.key == K_DOWN: player.move('down')
        
        if check_victory():
            key_text = "Press ENTER to reload or ESC to escape the game"
            display_text(main_window, key_text, (51,204,0) , 26, int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT*0.7))
            game_loop = False
            end_pause = True
        
        pygame.display.flip()
        
    while end_pause:
        
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    end_pause = False
                    game_loop = False
                    game_window = False
            if event.type == KEYDOWN and event.key == K_RETURN:
                    end_pause = False