import pygame 

from pygame.locals import *
from constants import *


class Level:
    # Level creation class
    def __init__(self, file):
        self.file = file
        self.structure = []
        self.begin_position = []
        self.end_position = []

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
                    tile = path
                # apply sprite in window at tile_position 
                window.blit(tile, tile_position)
                # move to the next tile on x-axis
                tile_x += TILE_SIZE
            # move to the next tile on y-axis
            tile_y += TILE_SIZE

       
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
    
    def test_collision(self, direction):
        not_collide = False
        # Check direction
        if direction == 'right':
            # Prevents Player from moving out of the screen
            if self.index_x < self.length_struct_x - 1:
                # Check if next tile is not a wall (horizontal)
                if self.level.structure[self.index_y][self.index_x + 1] != 'w':
                    # No Collision
                    not_collide = True
        elif direction == 'left':
            if self.index_x > 0:
                if self.level.structure[self.index_y][self.index_x - 1] != 'w':
                    not_collide = True
        elif direction == 'down':
            if self.index_y < self.length_struct_y - 1:
                # Check if next tile is not a wall (vertical)
                if self.level.structure[self.index_y + 1][self.index_x] != 'w':
                    # No Collision
                    not_collide = True
        elif direction == 'up':
            if self.index_y > 0:
                if self.level.structure[self.index_y - 1][self.index_x] != 'w':
                    not_collide = True
        else:
            # Collision
            not_collide = False
        # Return not_collide state
        return not_collide

    def move(self, direction):
        test_collision = self.test_collision(direction)
        # Check direction
        if test_collision:
            if direction == 'right':
                # move on next tile (horizontal)
                self.x += TILE_SIZE
            elif direction == 'left':
                # move on previous tile (horizontal)
                self.x -= TILE_SIZE
            elif direction == 'down':
                # move on next tile (vertical)
                self.y += TILE_SIZE
            elif direction == 'up':
                # move on previous tile (horizontal)
                self.y -= TILE_SIZE
        
        self.index_x = int(self.x / TILE_SIZE)
        self.index_y = int(self.y / TILE_SIZE)


class Guardian(Character):
    def __init__(self, sprite, level, position):
        super().__init__(sprite, level, position)
    
