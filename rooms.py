class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

# Example rooms
room_list = [
    Room("Living Room", "A cozy living room with a fireplace."),
    Room("Kitchen", "A spacious kitchen with a large dining table."),
    Room("Bedroom", "A comfortable bedroom with a queen-sized bed.")
]
