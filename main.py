import pygame
import os

from pygame.locals import *

import constants as const

from character import Player, Guardian
from item import Type, Item
from level import Level
from ui import UI


def create_item(item_type):
    """ Function used to instanciate items """
    itm = Item(item_type, level)
    itm.create()


def display_text(window, text, p_color, size, p_x=int(const.SCR_WIDTH/2),
                 p_y=int(const.GAME_SCR_HEIGHT/2), font=None):
    """ Function used to display some centered text at (px, py) position """
    font = pygame.font.Font(font, size)
    text = font.render(text, 1, p_color)
    text_rect = text.get_rect(center=(p_x, p_y))
    window.blit(text, text_rect)


def check_victory():
    """ End Game, victory or defeat conditions.. """
    if not player.is_weak and player.position == guard.position:
        MAIN_WINDOW.blit(BG_DARK, (0, 0))
        txt = "Congratulations !!! YOU WIN !!!"
        display_text(MAIN_WINDOW, txt, const.GOLD_COLOR, 40)
        return True
    if player.is_weak and player.position == guard.position:
        # Replace player sprite by grave sprite
        player.sprite = pygame.image.load(const.SPR_GRAVE).convert_alpha()
        player.x = player.x - const.TILE_SIZE  # Previous Tile position
        MAIN_WINDOW.blit(BG_DARK, (0, 0))  # Apply BG_DARK
        txt = "YOU LOSE !!!"
        display_text(MAIN_WINDOW, txt, const.RED_COLOR, 40)
        return True


# Centered game window
os.environ['SDL_VIDEO_CENTERED'] = '1'
# PyGame Initialization
pygame.init()
# Pygame Main Window
MAIN_WINDOW = pygame.display.set_mode((const.SCR_WIDTH, const.SCR_HEIGHT))
# Pygame Main Window Title
pygame.display.set_caption(const.TITLE_WINDOW)
# Dark Background
BG_DARK = pygame.image.load(const.BG_DARK).convert_alpha()

game_window = True
while game_window:  # Main Loop
    print('Loading...')
    # Init. Item list
    Item.instances_in_level = []
    # Init. UI Slots
    UI.list_slot_ui = []
    # Create level structure
    level = Level(const.LVL_LABYRINTH)
    level.gen_level()
    # Create Player
    player = Player(const.SPR_PLAYER, level, level.begin_position)
    # UI
    ui = UI(player, MAIN_WINDOW)
    ui.init_ui()
    # Create Guardian
    guard = Guardian(const.SPR_GUARD, level, level.end_position)
    # Items Creation
    create_item(Type.TUBE)
    create_item(Type.ETHER)
    create_item(Type.NEEDLE)
    print('Nb items in Level : ' + str(len(Item.instances_in_level)))
    print('...Ready')
    # Init Booleans
    end_pause = False
    game_loop = True
    while game_loop:  # Game Loop
        level.draw(MAIN_WINDOW)  # Draw Level
        ui.draw()  # Draw UI

        MAIN_WINDOW.blit(guard.sprite, (guard.x, guard.y))  # Draw Guardian
        for item in Item.instances_in_level:
            MAIN_WINDOW.blit(item.sprite, (item.position))  # Draw Items

        for event in pygame.event.get():
            # Events management
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                # Exit Game event
                game_loop = False
                game_window = False

            if event.type == KEYDOWN:
                # Inputs
                if event.key == K_RIGHT:
                    player.move('right')
                if event.key == K_LEFT:
                    player.move('left')
                if event.key == K_UP:
                    player.move('up')
                if event.key == K_DOWN:
                    player.move('down')

        if check_victory():  # end game conditions
            KEY_TEXT = "Press ENTER to reload or ESC to escape the game"
            display_text(MAIN_WINDOW, KEY_TEXT, const.GREEN_COLOR, 26,
                         int(const.SCR_WIDTH/2), int(const.SCR_HEIGHT*0.7))
            game_loop = False
            end_pause = True

        MAIN_WINDOW.blit(player.sprite, (player.x, player.y))
        pygame.display.flip()

    while end_pause:  # End Game Pause Loop
        for event in pygame.event.get():
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                end_pause = False
                game_loop = False
                game_window = False
            if event.type == KEYDOWN and event.key == K_RETURN:
                end_pause = False
