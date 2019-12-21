import pygame

from constants import *

class Slot:
    SLOT_SIZE = 64

    def __init__(self):
        self.sprite_slot = pygame.image.load(sprite_placeholder).convert_alpha()
        self.x = 0
        self.y = 0
        self.is_empty = True
    

class UI:
    INV_SLOT_SIZE = 64
    list_slot_ui = []

    def __init__(self, player):
        self.player = player
        self.nb_inv_slot = 3
        self.slot_pos_x = 16
        self.slot_pos_y = TILE_SIZE*15 + 16
        for i in range(self.nb_inv_slot):
            slot = Slot()
            slot.x = self.slot_pos_x
            slot.y = self.slot_pos_y
            UI.list_slot_ui.append(slot)
            self.slot_pos_x += UI.INV_SLOT_SIZE + 10

    def draw(self, ):
        print(len(UI.list_slot_ui))
        for slot in UI.list_slot_ui:
            self.window.blit(slot.sprite_slot, (slot.x, slot.y))
    
    def draw_in_slot(self, item):
        for slot in UI.list_slot_ui:
            if slot.is_empty:
                slot.is_empty = False
                self.window.blit(item.sprite, (slot.x, slot.y))
