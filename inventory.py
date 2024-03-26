class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} not found in inventory!")

    def display_inventory(self):
        if self.items:
            print("Inventory:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("Inventory is empty.")
