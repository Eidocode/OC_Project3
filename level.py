import pygame
import random

from pygame.locals import *
from constants import *

class Tile:
    tiles_in_level = []

    def __init__(self):
        self.position = (0, 0)
        self.sprite = pygame.image.load(sprite_path_1).convert()

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
        wall_1 = pygame.image.load(sprite_wall_1).convert()
        wall_2 = pygame.image.load(sprite_wall_2).convert()
        end = pygame.image.load(sprite_end).convert()
        path_1 = pygame.image.load(sprite_path_1).convert()
        path_2 = pygame.image.load(sprite_path_2).convert()

        walls = [wall_1, wall_2]
        paths = [path_1, path_2]

        for line in self.structure: # Scan level structure
            tile_x = 0 # Reset tile_x
            for sprite in line: # Scan sprite in line
                tile = Tile()
                # Check sprite ('b': Begin, 'w' : Wall, 'e' : end)
                if sprite == 'b':
                    tile.position = (tile_x, tile_y)
                    self.begin_position = tile.position
                    tile.sprite = begin
                elif sprite == 'w':
                    tile.position = (tile_x, tile_y)
                    wall_index = random.randrange(0, len(walls))
                    tile.sprite = walls[wall_index]
                elif sprite == 'e':
                    tile.position = (tile_x, tile_y)
                    self.end_position = tile.position
                    tile.sprite = end
                elif sprite == '0':
                    tile.position = (tile_x, tile_y)
                    self.item_placeholder.append(tile.position)
                    path_index = random.randrange(0, len(paths))
                    tile.sprite = paths[path_index]
                Tile.tiles_in_level.append(tile)
                tile_x += TILE_SIZE # move to the next tile on x-axis
            tile_y += TILE_SIZE # move to the next tile on y-axis

    def draw(self, window):
        for tile in Tile.tiles_in_level:
            window.blit(tile.sprite, tile.position) # apply sprite in window at tile_position 