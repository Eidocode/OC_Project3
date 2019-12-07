import pygame

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