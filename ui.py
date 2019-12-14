import pygame

from constants import *

class UI:
    INV_SLOT_SIZE = 96

    def __init__(self):
        self.inv_spr_placeholder = pygame.image.load(sprite_placeholder).convert_alpha()
        self.inv_pos_placeholder = (16, TILE_SIZE*15 + 16)


    def draw(self, window):
        inv_pos_x_placeholder = self.inv_pos_placeholder[0]
        inv_pos_y_placeholder = self.inv_pos_placeholder[1]
        for i in range(3):
            window.blit(self.inv_spr_placeholder, (inv_pos_x_placeholder, inv_pos_y_placeholder))
            inv_pos_x_placeholder += UI.INV_SLOT_SIZE + 10