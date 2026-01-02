from collections import OrderedDict

class LFUCache:
    # Priority is needed. 
    # But heapq operations expends O(log n) instead of O(1)
    # Native Counter also has O(log n) to query the least frequent element
    # => Must self implement a linked list to keep track of the least element
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freqs = OrderedDict()
        self.cache = {}
        self.min_freq = 0

    def _update_existing(self, key):
        val, freq = self.cache[key]

        # Remove it from current freqs list
        self.freqs[freq].pop(key)

        # Add it to next freqs list
        self.freqs.setdefault(freq + 1, OrderedDict())[key] = None # Value doesn't matter. Add the key is the aim.

        # Update the min_freq
        if not self.freqs[freq] and freq == self.min_freq:
            self.min_freq = freq + 1

        # Update cache
        self.cache[key] = (val, freq + 1)


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
                
        # Update frequency
        self._update_existing(key)
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        # if existing element => update freq and value
        if key in self.cache:
            self._update_existing(key)
            self.cache[key] = (value, self.cache[key][1])
        # if new element => Remove least, Add freq
        else:
            if len(self.cache) == self.capacity:
                # Remove min freq from freqs
                evict_key, _ = self.freqs[self.min_freq].popitem(last = False)
            
                # Remove min freq from cache
                del self.cache[evict_key]

            # Add to cache
            self.cache[key] = (value, 1)

            # Add to freqs
            self.freqs.setdefault(1, OrderedDict())[key] = None

            # Set min freq
            self.min_freq = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)