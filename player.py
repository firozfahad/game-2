from inventory import Inventory


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.inventory = Inventory()
