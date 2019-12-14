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
        self.sprite = pygame.image.load(sprite_end).convert()
        self.level = level
        self.index_position = random.randrange(0,len(self.level.item_placeholder))
        self.position = self.level.item_placeholder.pop(self.index_position)
        self.item_type = item_type
        self.is_drop = False

    def create(self):
        if self.item_type.value == 1:
            print('create tube')
            spr = sprite_item
        elif self.item_type.value == 2:
            print('create produit')
            spr = sprite_item
        elif self.item_type.value == 3:
            print("Create aiguille")
            spr = sprite_item
        elif self.item_type.value == 4:
            print("Create syringe")
            spr = sprite_item_s
        self.sprite = pygame.image.load(spr).convert()
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