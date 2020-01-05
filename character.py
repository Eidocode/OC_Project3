import pygame

from constants import TILE_SIZE
from inventory import Inventory
from item import Item


class Character:
    """
        Main class. Contains the sprite to display, coordinates (x, y) and some level informations..
    """
    def __init__(self, sprite, level, position):
        # Character sprite
        self.sprite = pygame.image.load(sprite).convert_alpha()
        # Character pixel position
        self.x = position[0]
        self.y = position[1]
        self.position = position
        # Character index position (on level structure)
        self.index_x = int(self.x / TILE_SIZE)
        self.index_y = int(self.y / TILE_SIZE)
        # Current Level
        self.level = level
        # Level structure length on x and y axis
        self.length_struct_x = len(self.level.structure[0])
        self.length_struct_y = len(self.level.structure)


class Player(Character):
    """
        Inherits from Character.
        Contains instance of Inventory class and a variable (is_weak) used for winning condition.
        There is also collisions tests (borders and walls) and items interaction. This tests are
        used when the player want to move in a direction.
    """
    def __init__(self, sprite, level, position):
        super().__init__(sprite, level, position)
        self.inventory = Inventory(self.level, self) # Init Player Inventory
        self.is_weak = True # Used for guardian interaction (winning condition)

    @property
    def right_border_collision(self):
        """ Test if player collide with screen right border """
        if self.index_x < self.length_struct_x - 1:
            return False
        return True

    @property
    def left_border_collision(self):
        """ Test if player collide with screen left border """
        if self.index_x > 0:
            return False
        return True

    @property
    def down_border_collision(self):
        """ Test if player collide with screen bottom border """
        if self.index_y < self.length_struct_y - 1:
            return False
        return True

    @property
    def up_border_collision(self):
        """ Test if player collide with screen upper border """
        if self.index_y > 0:
            return False
        return True

    def test_item_place(self):
        """ Check if there is an item on player position and interact """
        for item in Item.instances_in_level:
            if item.position == (self.x, self.y) and not item.is_drop:
                print(item.item_type.name + ' dropped')
                self.inventory.store_item(item)

    def test_if_tile_is_a_wall(self, ind_y, ind_x):
        """ Check if Tile with coordinates ind_y, ind_x is a Wall """
        if self.level.structure[ind_y][ind_x] == 'w':
            return True
        return False

    def test_collision(self, direction):
        """ Test all collisions(Borders and walls) and return True or False """
        collide = False
        if direction == 'right' and not self.right_border_collision:
            collide = self.test_if_tile_is_a_wall(self.index_y, self.index_x + 1)
        elif direction == 'left' and not self.left_border_collision:
            collide = self.test_if_tile_is_a_wall(self.index_y, self.index_x - 1)
        elif direction == 'down' and not self.down_border_collision:
            collide = self.test_if_tile_is_a_wall(self.index_y + 1, self.index_x)
        elif direction == 'up' and not self.up_border_collision:
            collide = self.test_if_tile_is_a_wall(self.index_y - 1, self.index_x)
        else:
            collide = True

        return collide # Return collide state

    def move(self, direction):
        """ Player move to 'direction' if there is no collision """
        test_collision = self.test_collision(direction) # Return if player collide in this direction
        if not test_collision: # Test collide and move if possible
            if direction == 'right':
                self.x += TILE_SIZE
            elif direction == 'left':
                self.x -= TILE_SIZE
            elif direction == 'down':
                self.y += TILE_SIZE
            elif direction == 'up':
                self.y -= TILE_SIZE

        self.position = (self.x, self.y) # Update player pixel coordinates
        # Update index x position (to use with level.structure)
        self.index_x = int(self.x / TILE_SIZE)
        self.index_y = int(self.y / TILE_SIZE)

        self.test_item_place() # Check if there is an item


class Guardian(Character):
    """
        Just inherits from Character without additional method. But, it's possible, later..
    """
    def __init__(self, sprite, level, position):
        super().__init__(sprite, level, position)
