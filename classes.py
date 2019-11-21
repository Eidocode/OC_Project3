import pygame 

from pygame.locals import *
from constantes import *


class Level:
    # Level creation class
    def __init__(self, file):
        self.file = file
        self.level_structure = []

    def read_level(self):
        # Get file content (*.lvl) and stock in a list (file_content)
        with open(self.file, "r") as file:
            file_content = []
            # Scan lines in file
            for line in file:
                line_content = []
                # Scan sprites in line
                for sprite in line:
                    # ignore line break
                    if sprite != '\n':
                        # add sprite to file_content
                        line_content.append(sprite)
                # add line to file_content
                file_content.append(line_content)
        # Save level_structure
        self.level_structure = file_content
    
    def gen_level(self, window):
        # Init. tile position (x, y)
        tile_x = 0
        tile_y = 0

        # Loads sprites used for level generation
        begin = pygame.image.load(sprite_begin).convert()
        wall = pygame.image.load(sprite_wall).convert()
        end = pygame.image.load(sprite_end).convert()

        # Scan level structure
        for line in self.level_structure:
            # Reset tile_x
            tile_x = 0
            # Scan sprite in line
            for sprite in line:
                # Check sprite ('b': Begin, 'w' : Wall, 'e' : end)
                if sprite == 'b':
                    tile_position = (tile_x, tile_y)
                    tile = begin
                elif sprite == 'w':
                    tile_position = (tile_x, tile_y)
                    tile = wall
                elif sprite == 'e':
                    tile_position = (tile_x, tile_y)
                    tile = end
                # apply sprite in window at tile_position 
                window.blit(tile, tile_position)
                # move to the next tile on x-axis
                tile_x += TILE_SIZE
            # move to the next tile on y-axis
            tile_y += TILE_SIZE

       
class Character:
    def __init(self):
        pass

