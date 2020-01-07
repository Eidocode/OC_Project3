import random

import pygame
import constants as const


class Tile:
    """
    Instances of this class are used in Level class and represents an element
    of the game. Each instance contains the position (x, y) and sprite of the
    tile. There is also a class variable 'tiles_in_level' where instances are
    stored.
    """
    tiles_in_level = []

    def __init__(self):
        self.position = (0, 0)
        self.sprite = pygame.image.load(const.SPR_PATH_1).convert()


class Level:
    """
    Level is generated here. '_read_level' method is first used to get level
    structure stored in a '.lvl' file. Then, this structure is stored in a
    variable and interpreted in a method called 'gen_level'.
    For each element of the structure, a tile is instanciated then a sprite and
    a position assigned to this tile instance. The tile is then stored in
    'tiles_in_level' which will be used for rendering the tiles sprites in
    'draw' method.
    """
    def __init__(self, file):
        self.file = file  # File where structure is stored
        self.structure = []  # Used to store level structure
        self.begin_position = []  # Level Begin position
        self.end_position = []  # Level End position
        self.item_location = []  # Store locations where items can spawn

    @property
    def _read_level(self):
        """ Get file content (*.lvl) and store structure in a list """
        with open(self.file, "r") as file:
            file_content = []
            for line in file:  # Scan lines in file
                line_content = []
                for sprite in line:  # Scan each element in line
                    if sprite != '\n':  # ignore line break
                        line_content.append(sprite)  # add to line_content
                # add line_content to file_content
                file_content.append(line_content)
        return file_content  # Return structure

    def gen_level(self):
        """ Assigns location and sprite of each tile according to the level
        structure """
        self.structure = self._read_level  # Apply _read_level to structure
        # Init. tile position (x, y)
        tile_x = 0
        tile_y = 0
        # Loads sprites
        begin = pygame.image.load(const.SPR_BEGIN).convert()
        end = pygame.image.load(const.SPR_END).convert()
        walls = [pygame.image.load(const.SPR_WALL_1).convert(),
                 pygame.image.load(const.SPR_WALL_2).convert()]
        paths = [pygame.image.load(const.SPR_PATH_1).convert(),
                 pygame.image.load(const.SPR_PATH_2).convert()]

        for line in self.structure:  # Scan lines in level structure
            tile_x = 0  # Reset tile_x
            for sprite in line:  # Scan sprite in line
                tile = Tile()  # Create a tile
                tile.position = (tile_x, tile_y)
                # Check sprite ('b': Begin, 'w' : Wall, 'e' : end, '0' : path)
                if sprite == 'b':
                    self.begin_position = tile.position
                    tile.sprite = begin
                elif sprite == 'w':
                    wall_index = random.randrange(0, len(walls))
                    tile.sprite = walls[wall_index]
                elif sprite == 'e':
                    self.end_position = tile.position
                    tile.sprite = end
                elif sprite == '0':
                    path_index = random.randrange(0, len(paths))
                    tile.sprite = paths[path_index]
                    self.item_location.append(tile.position)
                Tile.tiles_in_level.append(tile)
                tile_x += const.TILE_SIZE  # move to the next tile on x-axis
            tile_y += const.TILE_SIZE  # move to the next tile on y-axis

    def draw(self, window):
        """ Used to draw each tile stored in 'tiles_in_level' """
        for tile in Tile.tiles_in_level:
            # apply sprite in window at tile_position
            window.blit(tile.sprite, tile.position)
