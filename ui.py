import pygame

from constants import *

class Slot:
    SLOT_SIZE = 64

    def __init__(self):
        self.sprite_slot = pygame.image.load(sprite_placeholder).convert_alpha()
        self.x = 0
        self.y = 0
    

class UI:
    INV_SLOT_SIZE = 64

    def __init__(self):
        self.nb_inv_slot = 3
        self.slot_pos_x = 16
        self.slot_pos_y = TILE_SIZE*15 + 16

    def draw(self, window):
        slot_pos_x = self.slot_pos_x
        slot_pos_y = self.slot_pos_y

        for i in range(self.nb_inv_slot):
            slot = Slot()
            slot.x = slot_pos_x
            slot.y = slot_pos_y
            window.blit(slot.sprite_slot, (slot.x, slot.y))
            slot_pos_x += UI.INV_SLOT_SIZE + 10