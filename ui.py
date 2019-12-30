import pygame

from constants import *

class Slot:

    def __init__(self):
        self.sprite_slot = pygame.image.load(sprite_placeholder).convert_alpha()
        self.remove_sprite_in_slot = pygame.image.load(sprite_placeholder).convert()
        self.size = 64
        self.x = 0
        self.y = 0
        self.is_empty = True
    

class UI:
    list_slot_ui = []

    def __init__(self, player, window):
        self.player = player
        self.window = window
        self.nb_inv_slot = 3
        self.slot_pos_x = 16
        self.slot_pos_y = TILE_SIZE*15 + 16
        for i in range(self.nb_inv_slot):
            slot = Slot()
            slot.x = self.slot_pos_x
            slot.y = self.slot_pos_y
            UI.list_slot_ui.append(slot)
            self.slot_pos_x += slot.size + 10

    @property
    def add_special_slot(self):
        slot = Slot()
        slot.x = 258
        slot.y = self.slot_pos_y
        return slot

    def add_icon_in_slot(self, icon, alpha, slot):
        spr = pygame.image.load(icon).convert_alpha()
        spr.set_alpha(alpha)
        self.window.blit(spr, (slot.x + 8, slot.y + 8))

    def draw(self):
        special_slot = self.add_special_slot # ADD Special Item Slot
        self.window.blit(special_slot.sprite_slot, (special_slot.x, special_slot.y))
        if self.player.inventory.combine_items:
            self.add_icon_in_slot(sprite_seringue, 128, special_slot)
        else:
            self.window.blit(special_slot.remove_sprite_in_slot, (special_slot.x, special_slot.y))
            

        for slot in UI.list_slot_ui:
            self.window.blit(slot.sprite_slot, (slot.x, slot.y))
            if len(self.player.inventory.content) > 0:
                for item in self.player.inventory.content:
                    if slot.is_empty:
                        if not item.is_draw_ui:
                            slot.is_empty = False
                            item.is_draw_ui = True
                            self.add_icon_in_slot(item.ui_icon, 20, slot)
            else:
                self.window.blit(slot.remove_sprite_in_slot, (slot.x, slot.y))