import uuid
from datetime import datetime, timedelta, date

class FoodItem:
    def __init__(self, name, category, quantity, expiration_date, item_id=None, status="available"):
        self.id = item_id or str(uuid.uuid4())
        self.name = name
        self.category = category
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.status = status

    def is_expired(self):
        return datetime.now().date() > self.expiration_date

    def to_line(self):
        return f"{self.id}|{self.name}|{self.category}|{self.quantity}|{self.expiration_date.isoformat()}|{self.status}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split("|")
        if len(parts) != 6:
            return None
        item_id, name, category, quantity, exp_date_str, status = parts
        exp_date = datetime.strptime(exp_date_str, "%Y-%m-%d").date()
        return FoodItem(name, category, int(quantity), exp_date, item_id=item_id, status=status)

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
