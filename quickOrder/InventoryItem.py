class InventoryItem:
    def __init__(self, item_id, item_name, current_quantity, min_quantity, refill_needed):
        self.item_id = item_id
        self.item_name = item_name
        self.current_quantity = current_quantity
        self.min_quantity = min_quantity
        self.refill_needed = refill_needed

    def needsRefill(self): 
        if (self.current_quantity < self.min_quantity):
            self.refill_needed = True
        return self.refill_needed
