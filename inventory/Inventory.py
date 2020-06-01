class Inventory:
    def __init__(self, item_id,item_name,current_level, target_level, price,isOrdered, refillNeeded):
        self.item_id = item_id
        self.item_name = item_name
        self.current_level = current_level
        self.target_level = target_level
        self.price = price
        self.isOrdered = isOrdered
        self.refillNeeded = refillNeeded

    def __str__(self):
        return self.item_name

  