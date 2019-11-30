import pygame
import random

from pygame.locals import *
from constants import *


class Level: # Level creation class
    def __init__(self, file):
        self.file = file
        self.structure = []
        self.begin_position = []
        self.end_position = []
        self.item_placeholder = []

    @property
    def _read_level(self): # Get file content (*.lvl) and stock in a list (file_content)
        with open(self.file, "r") as file:
            file_content = []
            for line in file: # Scan lines in file
                line_content = []
                for sprite in line: # Scan sprites in line
                    if sprite != '\n': # ignore line break
                        line_content.append(sprite) # add sprite to file_content
                file_content.append(line_content) # add line to file_content
        return file_content # Save structure
    
    def gen_level(self, window):
        self.structure = self._read_level # Apply _read_level to structure
        # Init. tile position (x, y)
        tile_x = 0
        tile_y = 0
        # Loads sprites used for level generation
        begin = pygame.image.load(sprite_begin).convert()
        wall = pygame.image.load(sprite_wall).convert()
        end = pygame.image.load(sprite_end).convert()
        path = pygame.image.load(sprite_path).convert()

        for line in self.structure: # Scan level structure
            tile_x = 0 # Reset tile_x
            
            for sprite in line: # Scan sprite in line
                # Check sprite ('b': Begin, 'w' : Wall, 'e' : end)
                if sprite == 'b':
                    tile_position = (tile_x, tile_y)
                    self.begin_position = tile_position
                    tile = begin
                elif sprite == 'w':
                    tile_position = (tile_x, tile_y)
                    tile = wall
                elif sprite == 'e':
                    tile_position = (tile_x, tile_y)
                    self.end_position = tile_position
                    tile = end
                elif sprite == '0':
                    tile_position = (tile_x, tile_y)
                    self.item_placeholder.append(tile_position)
                    tile = path
                window.blit(tile, tile_position) # apply sprite in window at tile_position 
                tile_x += TILE_SIZE # move to the next tile on x-axis
            tile_y += TILE_SIZE # move to the next tile on y-axis

       
class Character:
    def __init__(self, sprite, level, position):
        # Character sprite
        self.sprite = pygame.image.load(sprite).convert_alpha()
        # Character pixel position
        self.x = position[0]
        self.y = position[1]
        # Character index position (on level structure)
        self.index_x = int(self.x / TILE_SIZE)
        self.index_y = int(self.y / TILE_SIZE)
        # Current Level
        self.level = level
        # Structure length on x and y axis
        self.length_struct_x = len(self.level.structure[0])
        self.length_struct_y = len(self.level.structure)

class Player(Character):
    def __init__(self, sprite, level, position):
        super().__init__(sprite, level, position)

    @property
    def right_border_collision(self): # Test if player collide with screen right border
        if (self.index_x < self.length_struct_x - 1) : return False
        return True
    
    @property
    def left_border_collision(self): # Test if player collide with left right border
        if (self.index_x > 0) : return False
        return True
    
    @property
    def down_border_collision(self): # Test if player collide with screen down border
        if (self.index_y < self.length_struct_y - 1) : return False
        return True
    
    @property
    def up_border_collision(self): # Test if player collide with screen upper border
        if (self.index_y > 0) : return False
        return True
    
    def test_item_place(self):
        for item in Item.instances:
            if item.position == (self.x, self.y) and item.is_drop == False:
                print('There is an item')
                item.drop()


    def test_if_tile_is_a_wall(self, ind_y, ind_x):
        if self.level.structure[ind_y][ind_x] == 'w':
            return True
        else:
            return False

    def test_collision(self, direction):
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

        return collide  # Return collide state

    def move(self, direction):
        test_collision = self.test_collision(direction) # Test if collide in this direction
        if not test_collision:
            if direction == 'right': self.x += TILE_SIZE  # move on next tile (horizontal)
            elif direction == 'left': self.x -= TILE_SIZE  # move on previous tile (horizontal)
            elif direction == 'down': self.y += TILE_SIZE  # move on next tile (vertical)
            elif direction == 'up': self.y -= TILE_SIZE  # move on previous tile (vertical)

        self.index_x = int(self.x / TILE_SIZE)
        self.index_y = int(self.y / TILE_SIZE)

        self.test_item_place()


class Guardian(Character):
    def __init__(self, sprite, level, position):
        super().__init__(sprite, level, position)
    

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
        self.sprite = pygame.image.load(spr).convert()
        Item.instances.append(self)
    
    def drop(self):
        self.is_drop = True
        if self.is_drop:
            self.sprite = pygame.image.load(sprite_end).convert()



        
