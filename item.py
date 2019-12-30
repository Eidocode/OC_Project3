import pygame
import random

from enum import Enum
from constants import *

class Type(Enum):
    TUBE = 1
    PRODUIT = 2
    AIGUILLE = 3
    SERINGUE = 4


class Item:
    instances_in_level = []

    def __init__(self, item_type, level):
        self.sprite = pygame.image.load(sprite_item).convert_alpha()
        self.ui_icon = sprite_item_s
        self.level = level
        self.index_position = random.randrange(0,len(self.level.item_placeholder))
        self.position = self.level.item_placeholder.pop(self.index_position)
        self.item_type = item_type
        self.is_draw_ui = False
        self.is_drop = False

    def create(self):
        if self.item_type == Type.TUBE:
            print('create tube')
            spr = sprite_tube
        elif self.item_type == Type.PRODUIT:
            print('create produit')
            spr = sprite_ether
        elif self.item_type == Type.AIGUILLE:
            print("Create aiguille")
            spr = sprite_aiguille
        # elif self.item_type.value == Type.SERINGUE:
        #     print("Create syringe")
        #     spr = sprite_seringue
        self.ui_icon = spr
        Item.instances_in_level.append(self)
    
    def drop(self):
        self.is_drop = True
        self._destroy

    @property
    def _destroy(self):
        print(str(self) + ' has been destroyed.')
        Item.instances_in_level.remove(self)
        print('Nb items in Level : ' + str(len(Item.instances_in_level)))
        del self