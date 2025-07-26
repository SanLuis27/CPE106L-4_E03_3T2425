from datetime import datetime, timedelta, date
from food_donation import FoodItem

class InventoryManager:
    def __init__(self, filepath="inventory.txt"):
        self.filepath = filepath
        self.inventory = []
        self.load_inventory()

    def add_item(self, food_item):
        self.inventory.append(food_item)
        self.save_inventory()

    def get_available_items(self):
        self.remove_expired_items()
        return [item for item in self.inventory if item.status == "available"]

    def remove_expired_items(self):
        changed = False
        for item in self.inventory:
            if item.status == "available" and item.is_expired():
                item.status = "expired"
                changed = True
        if changed:
            self.save_inventory()

    def mark_item_as_delivered(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                item.status = "delivered"
                self.save_inventory()
                break

    def save_inventory(self):
        with open(self.filepath, "w") as f:
            for item in self.inventory:
                f.write(item.to_line())

    def load_inventory(self):
        try:
            with open(self.filepath, "r") as f:
                self.inventory = []
                for line in f:
                    item = FoodItem.from_line(line)
                    if item:
                        self.inventory.append(item)
        except FileNotFoundError:
            self.inventory = []
