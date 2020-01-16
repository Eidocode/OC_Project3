class Inventory:
    """
    Instantiated in Player class. Contains a list (content) where all picked up
    items are stored. Variable (combine_items) is used and turns True when all
    items have been picked up.
    """
    def __init__(self, level, player):
        self.content = []  # List Inventory Content
        self.level = level
        self.player = player
        self.combine_items = False  # True if all items are picked up

    def store_item(self, item):
        """ Called when player interacts with an item.
        This method adds the item in 'content' list and calls a method of item
        instance.
        """
        print('store ' + item.item_type.name + ' to Player inventory.')
        self.content.append(item)  # Add Item to Inventory List
        item.pick_up()  # Item instance Method for item picking up
        self.get_content()
        if self.combine_items:
            self.player.is_weak = False  # If items are combined

    def get_content(self):
        """ Called in store_item method.
        Get the inventory content and turns True 'combine_items' if 3 items are
        picked up
        """
        print(str(len(self.content)) + ' items in Player inventory.')
        for item in self.content:
            print(item.item_type.name)
        if len(self.content) == 3:
            self.combine_items = True  # Combine Items if they're all picked-up
