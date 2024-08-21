def __init__(self, id, name, category, price, available=True):
self.id = id
self.name = name
        self.category = category
        self.price = price
        self.available = available
 
    def update(self, name=None, category=None, price=None, available=None):
        if name:
self.name = name
        if category:
            self.category = category
        if price:
            self.price = price
        if available is not None:
            self.available = available
 
    def to_dict(self):
        return {
"id": self.id,
"name": self.name,
            "category": self.category,
            "price": self.price,
            "available": self.available
        }
 
    @staticmethod
    def from_dict(data):
        return Product(
            id=data.get("id"),
            name=data.get("name"),
            category=data.get("category"),
            price=data.get("price"),
            available=data.get("available", True)
        )