from constants import *
from inventory import *
from item import *

class Character:
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
        # Structure length on x and y axis
        self.length_struct_x = len(self.level.structure[0])
        self.length_struct_y = len(self.level.structure)

class Player(Character):
    def __init__(self, sprite, level, position):
        super().__init__(sprite, level, position)
        # Init Player Inventory
        self.inventory = Inventory(self.level, self)
        # Used for guardian interaction
        self.is_weak = True

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
        for item in Item.instances_in_level:
            if item.position == (self.x, self.y) and item.is_drop == False:
                print(item.item_type.name + ' dropped')
                self.inventory.store_item(item)
    
    def check_items_in_inventory(self):
        if self.inventory.combine_items:
            self.inventory.combine_items_in_inventory()
    
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

        self.position = (self.x, self.y)
        self.index_x = int(self.x / TILE_SIZE)
        self.index_y = int(self.y / TILE_SIZE)

        self.check_items_in_inventory()
        self.test_item_place()


class Guardian(Character):
    def __init__(self, sprite, level, position):
        super().__init__(sprite, level, position)