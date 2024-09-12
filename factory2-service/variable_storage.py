class VariableStorage:
    def __init__(self, max_capacity, num_parts=6):
        self.max_capacity = max_capacity
        self.part_stock = [max_capacity] * num_parts

    def consume_part(self, part_index):
        if self.part_stock[part_index] > 0:
            self.part_stock[part_index] -= 1
            return True
        return False

    def can_produce(self, part_index):
        return self.part_stock[part_index] > 0
