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
        pass


class Character:
    def __init(self):
        pass

