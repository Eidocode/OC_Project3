import pygame 

from item import *
from ui import *

class Inventory:

    def __init__(self, level, player):
        self.content = []
        self.level = level
        self.player = player
        self.combine_items = False

    def store_item(self, item):
        print('store ' + item.item_type.name + ' to Player inventory.')
        self.content.append(item)
        item.drop()
        self.get_content()
        if item.item_type.value == 4:
            self.player.is_weak = False
    
    def get_content(self):
        print('There is ' + str(len(self.content)) + ' items in Player inventory.')
        for item in self.content:
            print(item.item_type.name)
        if len(self.content) == 3:
            self.content = []
            self.combine_items = True
            print("Inventory is empty..")
    
    def combine_items_in_inventory(self):
        syringe = Item(Type.SERINGUE, self.level)
        syringe.create()
        self.store_item(syringe)
        print(Item.instances_in_level)
        self.combine_items = False
