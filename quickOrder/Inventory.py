class Inventory:
    def __init__(self, item_id, item_name, current_quantity, min_quantity, isOrdered, status, refillNeeded):
        self.item_id = item_id
        self.item_name = item_name
        self.current_quantity = current_quantity
        self.min_quantity = min_quantity
        self.isOrdered = isOrdered
        self.status = status
        self.refillNeeded = refillNeeded

    def needsRefill(self): 
        if (self.current_quantity < self.min_quantity):
            self.refillNeeded = true
        return self.refillNeeded
        