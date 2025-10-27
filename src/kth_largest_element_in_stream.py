from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.sorted = nums
        heapq.heapify(self.sorted)

        while len(self.sorted) > k :
            heapq.heappop(self.sorted)

    def add(self, val: int) -> int:
        if len(self.sorted) < self.k:
            heapq.heappush(self.sorted, val)
        elif val > self.sorted[0]:
            heapq.heapreplace(self.sorted, val)

        return self.sorted[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)