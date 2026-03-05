import random


class RandomizedSet:
    # Use a list for O(1) random access and a hashmap for O(1) lookup
    # For removal: swap with last element, then pop

    def __init__(self):
        self.vals = []  # List of values
        self.idx_map = {}  # val -> index in vals

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        # Swap val with last element
        idx = self.idx_map[val]
        last_val = self.vals[-1]
        self.vals[idx] = last_val
        self.idx_map[last_val] = idx
        # Remove last element
        self.vals.pop()
        del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)