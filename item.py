import random

from enum import Enum

import pygame
import constants as const


class Type(Enum):
    """
        Used in Item class to identify an item type and for code understanding.
        Allows to use Type.TUBE (for example).
    """
    TUBE = 1
    ETHER = 2
    NEEDLE = 3


class Item:
    """
    Used for items to pick up in game level. Each instance contains a sprite
    and an ui_icon (used in ui.py) that is used in UI inventory when player
    picked up this item.There is also a random position used to place the item
    in the maze. 'is_draw_ui' variable is used in ui.py when 'ui_icon' has been
    drawn in UI Inventory. 'is_drop' variable is used in Player class
    (character.py) to picking up the item. Class variable (instances_in_level)
    contains Item instances and used to draw item sprite in main.py.
    """
    instances_in_level = []

    def __init__(self, item_type, level):
        self.sprite = pygame.image.load(const.SPR_ITEM).convert_alpha()
        self.ui_icon = const.SPR_ITEM_S  # Sprite used in UI Inventory
        self.level = level
        # Generate a random index linked to 'item_location' list
        self.index_position = random.randrange(0,
                                               len(self.level.item_location))
        # Assigns to 'position' the element identified by 'index_position'
        #  of 'item_location' list.
        self.position = self.level.item_location.pop(self.index_position)
        self.item_type = item_type  # Type of item designated by Enum Type
        self.is_draw_ui = False
        self.is_drop = False

    def create(self):
        """ This method assigns a sprite (ui_icon) to the instance based on
        item_type and add it to the class variable (instances_in_level) """
        if self.item_type == Type.TUBE:
            print('create tube')
            spr = const.SPR_TUBE
        elif self.item_type == Type.ETHER:
            print('create ether')
            spr = const.SPR_ETHER
        elif self.item_type == Type.NEEDLE:
            print("Create needle")
            spr = const.SPR_NEEDLE
        self.ui_icon = spr  # Assigns sprite to ui_icon
        Item.instances_in_level.append(self)  # Add to 'instances_in_level'

    def pick_up(self):
        """ Called in Inventory class (store_item method).
        Turns True is_drop and calls _destroy method. """
        self.is_drop = True
        self._destroy

    @property
    def _destroy(self):
        """ Called in pick_up method. Remove this instance itself and from
        'instances_in_level'. """
        print(str(self) + ' has been destroyed.')
        Item.instances_in_level.remove(self)  # Remove in 'instances_in_level'
        del self  # Remove instance itself
