import numpy as np
from variable_assembly_line import VariableAssemblyLine
from variable_storage import VariableStorage

class Factory2:
    def __init__(self, num_lines, storage_capacity, num_parts=6):
        self.storage = VariableStorage(storage_capacity, num_parts)
        default_product_type = 0
        self.lines = [VariableAssemblyLine(self.storage, default_product_type) for _ in range(num_lines)]

    def generate_random_binomial(self):
        result = np.random.binomial(52, 44.0 / 52.0)
        return int(result)

    def run_production(self, product_types):
        total_produced = 0
        actual_lines = min(len(self.lines), len(product_types))

        for i in range(actual_lines):
            product_to_produce = product_types[i]
            for _ in range(product_to_produce):
                produced = self.lines[i].produce(i)
                total_produced += produced

                if not self.storage.can_produce(i):
                    break

        return total_produced

    def display_status(self):
        self.storage.display_status()

    def get_storage(self):
        return self.storage
