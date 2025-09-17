from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.repo = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.repo:
            return -1
        
        val = self.repo[key]
        self.put(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.repo:
            del self.repo[key]
        self.repo[key] = value
        if len(self.repo) > self.capacity:
            # Removed the overspilled
            self.repo.popitem(last=False)

        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)