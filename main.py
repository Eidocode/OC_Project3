"""*
    TO DO : 
        - Redimensionner les sprites Openclassrooms
        - Créer un fichier / Class 
        - Appliquer PEP8
        - Ajouter Player Inventory
        - Fin du jeu (victoire ou défaite)
"""

import pygame
import random

from pygame.locals import *
from constants import *
from classes import *

def create_item(item_type):
    item = Item(item_type, level)
    item.create()

pygame.init()

# Pygame Main Window
main_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Pygame Main Window Custom
pygame.display.set_caption(TITLE_WINDOW)

# Create level structure
level = Level(LVL_LABYRINTH)
level.gen_level(main_window)
# Create Player
player = Player(sprite_player, level, level.begin_position)
# Create Guardian
guard = Guardian(sprite_guard, level, level.end_position)

# Items Creation
create_item('tube')
create_item('produit')
create_item('aiguille')
print('Nb items in Level : ' + str(len(Item.instances)))
print(Item.instances)

# Main Loop (Game Loop)
game_loop = True
while game_loop:
    
    level.gen_level(main_window)

    for item in Item.instances:
      main_window.blit(item.sprite, (item.position))
    main_window.blit(guard.sprite, (guard.x, guard.y))
    main_window.blit(player.sprite, (player.x, player.y))

    # --- Debug ---
    # print('px : ' + str(guard.x) + ', ' + str(guard.y))
    # print('index : ' + str(guard.index_x) + ', ' + str(guard.index_y))

    for event in pygame.event.get():
        # If player want to quit the game, game_loop = False
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            game_loop = False

        if event.type == KEYDOWN:
            if event.key == K_RIGHT: player.move('right')
            if event.key == K_LEFT: player.move('left')
            if event.key == K_UP: player.move('up')
            if event.key == K_DOWN: player.move('down')

    pygame.display.flip()