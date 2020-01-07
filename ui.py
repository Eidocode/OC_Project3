import pygame
import constants as const


class Slot:
    """
    Instanciated in UI class. Contains the sprite slot depending on it is empty
    or not. There is slot size, position and state (empty or not)
    """
    def __init__(self):
        self.sprite_slot = pygame.image.load(const.SPR_SLOT).convert_alpha()
        self.empty_sprite_slot = pygame.image.load(const.SPR_SLOT).convert()
        self.size = const.UI_SLOT_SIZE
        self.x = 0
        self.y = 0
        self.is_empty = True


class UI:
    """
    This class represents User Interface. It contains the inventory slots where
    the items are displayed and the player and guardian states. There is also
    the special slot where the syringe is diplayed when the 3 items have been
    picked up.
    """
    list_slot_ui = []  # List where UI slots are stored

    def __init__(self, player, window):
        self.player = player
        self.window = window
        self.nb_inv_slot = 3  # Number of Inventory Slots
        self.slot_pos_x = 16  # Slot x position
        self.slot_pos_y = const.UI_SLOT_POS_Y  # Slot y position

    def init_ui(self):
        """ Method called in main.py to initialize UI """
        for slot in range(self.nb_inv_slot):
            slot = Slot()
            slot.x = self.slot_pos_x  # Assigns slot_pos_x to slot.x
            slot.y = self.slot_pos_y
            UI.list_slot_ui.append(slot)  # Adds slot to 'list_slot_ui'
            self.slot_pos_x += slot.size + 10  # Modif slot_pos_x for next slot

    @property
    def add_special_slot(self):
        """ Method used to create the special slot """
        slot = Slot()
        slot.sprite_slot = pygame.image.load(const.SPR_SP_SLOT).convert_alpha()
        slot.x = const.UI_SLOT_SIZE * 8
        slot.y = self.slot_pos_y
        return slot

    def add_char_picture(self, sprite, x, y, lifebar_type):
        """ Add picture and lifebar at the specified location (x, y) """
        spr_picture = pygame.image.load(sprite).convert_alpha()
        spr_lifebar_full = pygame.image.load(const.SPR_LIFEBAR_FULL).convert()
        spr_lifebar_weak = pygame.image.load(const.SPR_LIFEBAR_WEAK).convert()
        offset = 50

        self.window.blit(spr_picture, (x, y))
        # choice between the two lifebar depending on 'lifebar_type'
        if lifebar_type == 0:
            self.window.blit(spr_lifebar_full, (x+offset, y))
        elif lifebar_type == 1:
            self.window.blit(spr_lifebar_weak, (x+offset, y))

    def add_icon_in_slot(self, icon, slot):
        """ Add a sprite (icon) in UI Slot (slot) """
        spr = pygame.image.load(icon).convert_alpha()
        self.window.blit(spr, (slot.x + const.OFFSET_CENTER_SLOT,
                               slot.y + const.OFFSET_CENTER_SLOT))

    def draw(self):
        """ Method used to draw all UI elements """
        # Special Slot
        special_slot = self.add_special_slot  # Create Special Slot
        self.window.blit(special_slot.sprite_slot,
                         (special_slot.x, special_slot.y))  # Draw Special Slot
        if self.player.inventory.combine_items:
            self.add_icon_in_slot(const.SPR_SYRINGE, special_slot)
        else:
            self.window.blit(special_slot.empty_sprite_slot,
                             (special_slot.x, special_slot.y))

        # Normal slots stored in 'list_slot_ui'
        for slot in UI.list_slot_ui:
            self.window.blit(slot.sprite_slot, (slot.x, slot.y))  # Draw slot
            # Check if inventory is not empty
            if len(self.player.inventory.content) > 0:
                for item in self.player.inventory.content:
                    if slot.is_empty:
                        if not item.is_draw_ui:
                            slot.is_empty = False
                            item.is_draw_ui = True
                            # Add item icon to UI slot
                            self.add_icon_in_slot(item.ui_icon, slot)
            else:
                # Add Empty slot
                self.window.blit(slot.empty_sprite_slot, (slot.x, slot.y))

        # Characters UI pictures and lifebars
        player_ui_pos_x = const.UI_SLOT_SIZE * 7 - 10
        guard_ui_pos_x = const.UI_SLOT_SIZE * 9 + 15
        picture_ui_pos_y = const.UI_SLOT_POS_Y + const.OFFSET_CENTER_SLOT

        if not self.player.is_weak:
            self.add_char_picture(const.SPR_UI_MCGYVER,
                                  player_ui_pos_x, picture_ui_pos_y, 0)
            self.add_char_picture(const.SPR_UI_GUARD,
                                  guard_ui_pos_x, picture_ui_pos_y, 1)
        else:
            self.add_char_picture(const.SPR_UI_MCGYVER,
                                  player_ui_pos_x, picture_ui_pos_y, 1)
            self.add_char_picture(const.SPR_UI_GUARD,
                                  guard_ui_pos_x, picture_ui_pos_y, 0)
