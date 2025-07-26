import uuid
from datetime import datetime

class FoodItem:
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
    def __init__(self, name, category, quantity, expiration_date, item_id=None, status="available"):
        self.id = item_id or str(uuid.uuid4())
        self.name = name
        self.category = category
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.status = status

    def is_expired(self):
        return datetime.now().date() > self.expiration_date

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "expiration_date": self.expiration_date.isoformat(),
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return FoodItem(
            name=data["name"],
            category=data["category"],
            quantity=data["quantity"],
            expiration_date=datetime.strptime(data["expiration_date"], "%Y-%m-%d").date(),
            item_id=data.get("id"),
            status=data.get("status", "available")
        )

class Donation:
    def __init__(self, donor, food_item, date_donated=None, donation_id=None):
        self.donation_id = donation_id or str(uuid.uuid4())
        self.donor = donor  # string or user id
        self.food_item = food_item  # instance of FoodItem
        self.date_donated = date_donated or datetime.now()

    def to_dict(self):
        return {
            "donation_id": self.donation_id,
            "donor": self.donor,
            "food_item": self.food_item.to_dict(),
            "date_donated": self.date_donated.isoformat()
        }

    @staticmethod
    def from_dict(data):
        return Donation(
            donor=data["donor"],
            food_item=FoodItem.from_dict(data["food_item"]),
            date_donated=datetime.fromisoformat(data["date_donated"]),
            donation_id=data.get("donation_id")
        )
