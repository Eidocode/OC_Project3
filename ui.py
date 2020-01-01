import pygame

from constants import *

class Slot:
    def __init__(self):
        self.sprite_slot = pygame.image.load(sprite_placeholder).convert_alpha()
        self.remove_sprite_in_slot = pygame.image.load(sprite_placeholder).convert()
        self.size = UI_SLOT_SIZE
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
        self.slot_pos_y = UI_SLOT_POS_Y
        for i in range(self.nb_inv_slot):
            slot = Slot()
            slot.x = self.slot_pos_x
            slot.y = self.slot_pos_y
            UI.list_slot_ui.append(slot)
            self.slot_pos_x += slot.size + 10

    @property
    def add_special_slot(self):
        slot = Slot()
        slot.sprite_slot = pygame.image.load(sprite_spec_placeholder).convert_alpha()
        slot.x = UI_SLOT_SIZE * 8
        slot.y = self.slot_pos_y
        return slot
    
    def add_character_picture(self, sprite, x, y, lifebar_type):
        spr_picture = pygame.image.load(sprite).convert_alpha()
        spr_lifebar_full = pygame.image.load(sprite_lifebar_full).convert_alpha()
        spr_lifebar_weak = pygame.image.load(sprite_lifebar_weak).convert_alpha()
        offset = 50

        self.window.blit(spr_picture, (x,y))
        if lifebar_type == 0:
            self.window.blit(spr_lifebar_full, (x+offset, y))
        elif lifebar_type == 1:
            self.window.blit(spr_lifebar_weak, (x+offset, y))
        elif lifebar_type == 2:
            self.window.blit(spr_lifebar_empty, (x+offset, y))

    def add_icon_in_slot(self, icon, slot):
        spr = pygame.image.load(icon).convert_alpha()
        self.window.blit(spr, (slot.x + OFFSET_CENTER_SLOT, slot.y + OFFSET_CENTER_SLOT))

    def draw(self):
        special_slot = self.add_special_slot # ADD Special Item Slot
        self.window.blit(special_slot.sprite_slot, (special_slot.x, special_slot.y))
        if self.player.inventory.combine_items:
            self.add_icon_in_slot(sprite_seringue, special_slot)
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
                            self.add_icon_in_slot(item.ui_icon, slot)
            else:
                self.window.blit(slot.remove_sprite_in_slot, (slot.x, slot.y))

        
        # Characters UI pictures and lifebars
        player_ui_pos_x = UI_SLOT_SIZE * 7 - 10
        guard_ui_pos_x = UI_SLOT_SIZE * 9 + 15
        picture_ui_pos_y = UI_SLOT_POS_Y + OFFSET_CENTER_SLOT

        if not self.player.is_weak:
            self.add_character_picture(sprite_ui_mcgyver, player_ui_pos_x, picture_ui_pos_y, 0)
            self.add_character_picture(sprite_ui_guard, guard_ui_pos_x, picture_ui_pos_y, 1)
        else:
            self.add_character_picture(sprite_ui_mcgyver, player_ui_pos_x, picture_ui_pos_y, 1)
            self.add_character_picture(sprite_ui_guard, guard_ui_pos_x, picture_ui_pos_y, 0)