import pygame
import random

from constants import *

class Item:
    instances = []

    def __init__(self, item_type, level):
        self.sprite = pygame.image.load(sprite_end).convert()
        self.level = level
        self.index_position = random.randrange(0,len(self.level.item_placeholder))
        self.position = self.level.item_placeholder.pop(self.index_position)
        self.item_type = item_type
        self.is_drop = False

    def create(self):
        if self.item_type == 'tube':
            print('create tube')
            spr = sprite_item
        elif self.item_type == 'produit':
            print('create produit')
            spr = sprite_item
        elif self.item_type == 'aiguille':
            print("Create aiguille")
            spr = sprite_item
        elif self.item_type == 'seringue':
            print("Create syringe")
            spr = sprite_item_s
        self.sprite = pygame.image.load(spr).convert()
        Item.instances.append(self)
    
    def drop(self):
        self.is_drop = True
        self._destroy

    @property
    def _destroy(self):
        print(str(self) + ' has been destroyed.')
        Item.instances.remove(self)
        print('Nb items in Level : ' + str(len(Item.instances)))
        del self