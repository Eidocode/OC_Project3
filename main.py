"""
    1 - Créer le cadre de départ

        Initialisez un repo Git et envoyez-le sur Github.
        Commencez par créer le labyrinthe sans l’interface graphique. Quand la logique de votre labyrinthe est faite, 
    utilisez le module PyGame pour dessiner l’interface graphique.
        Puis intéressez-vous aux trois éléments principaux du jeu : le gardien, MacGyver et les objets. Comment les représenter dans votre programme ? 
    Où sont-ils placés au commencement du jeu ? 

    2 - Animer le personnage

        Le seul élément mouvant est MacGyver. Créez les méthodes de classe qui permettent de l'animer et de trouver la sortie. 
    Pour l'instant, faites une version simplifiée du jeu dans laquelle MacGyver gagne en arrivant face au gardien.
 
    3 - Récupérer les objets

        Ajoutez la gestion des objets. Comment MacGyver les ramasse-t-il ?  Ajoutez également un compteur qui les listera.
 
    4 - Gagner !

        Enfin, changez la fin du jeu : MacGyver gagne s'il a bien ramassé tous les objets et endormi le garde. Sinon, il perd.
"""

import pygame

from pygame.locals import *
from constants import *
from classes import *

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

# Main Loop (Game Loop)
game_loop = True
while game_loop:
    
    level.gen_level(main_window)
    main_window.blit(player.sprite, (player.x, player.y))
    main_window.blit(guard.sprite, (guard.x, guard.y))

    # --- Debug ---
    # print('px : ' + str(guard.x) + ', ' + str(guard.y))
    # print('index : ' + str(guard.index_x) + ', ' + str(guard.index_y))

    for event in pygame.event.get():
        # If player want to quit the game, game_loop = False
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            game_loop = False
        
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player.move('right')
            if event.key == K_LEFT:
                player.move('left')
            if event.key == K_UP:
                player.move('up')
            if event.key == K_DOWN:
                player.move('down')

    pygame.display.flip()