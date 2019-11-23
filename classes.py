import pygame 

from pygame.locals import *
from constants import *


class Level:
    # Level creation class
    def __init__(self, file):
        self.file = file
        self.structure = []

    @property
    def _read_level(self):
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
        # Save structure
        return file_content
    
    def gen_level(self, window):
        # Apply _read_level to structure
        self.structure = self._read_level
        # Init. tile position (x, y)
        tile_x = 0
        tile_y = 0
        # Loads sprites used for level generation
        begin = pygame.image.load(sprite_begin).convert()
        wall = pygame.image.load(sprite_wall).convert()
        end = pygame.image.load(sprite_end).convert()
        path = pygame.image.load(sprite_path).convert()

        # Scan level structure
        for line in self.structure:
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
                elif sprite == '0':
                    tile_position = (tile_x, tile_y)
                    tile = path
                # apply sprite in window at tile_position 
                window.blit(tile, tile_position)
                # move to the next tile on x-axis
                tile_x += TILE_SIZE
            # move to the next tile on y-axis
            tile_y += TILE_SIZE

       
class Character:
    def __init__(self, sprite, level):
        # Character sprite
        self.sprite = pygame.image.load(sprite).convert_alpha()
        # Character pixel position
        self.x = 0
        self.y = 0
        # Character index position (on level structure)
        self.index_x = 0
        self.index_y = 0
        # Current Level
        self.level = level


class Player(Character):
    def __init__(self, sprite, level):
        super().__init__(sprite, level)
    
    def move(self, direction):
        # Check direction
        if direction == 'right':
            # Prevents Player from moving out of the screen
            if self.index_x < int(len(self.level.structure[0])) - 1:
                # Chech if next tile is not a wall (horizontal)
                if self.level.structure[self.index_y][self.index_x + 1] != 'w':
                    # move on next tile (horizontal)
                    self.x += TILE_SIZE
        elif direction == 'left':
            # Prevents Player from moving out of the screen
            if self.index_x > 0:
                # Chech if previous tile is not a wall (horizontal)
                if self.level.structure[self.index_y][self.index_x - 1] != 'w':
                    # move on previous tile (horizontal)
                    self.x -= TILE_SIZE
        elif direction == 'up':
            # Prevents Player from moving out of the screen
            if self.index_y > 0:
                # Chech if previous tile is not a wall (vertical)
                if self.level.structure[self.index_y - 1][self.index_x] != 'w':
                    # move on previous tile (vertical)
                    self.y -= TILE_SIZE
        elif direction == 'down':
            # Prevents Player from moving out of the screen
            if self.index_y < int(len(self.level.structure)) - 1:
                # Chech if next tile is not a wall (vertical)
                if self.level.structure[self.index_y + 1][self.index_x] != 'w':
                    # move on next tile (vertical)
                    self.y += TILE_SIZE
        
        self.index_x = int(self.x / TILE_SIZE)
        self.index_y = int(self.y / TILE_SIZE)


