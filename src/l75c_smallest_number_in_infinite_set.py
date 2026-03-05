import heapq

class SmallestInfiniteSet:
    # Approach:
    # Track the "frontier" - the smallest number never popped.
    # Use a min-heap + set for numbers added back (below frontier).
    
    # Time Complexity:
    # - popSmallest: O(log n)
    # - addBack: O(log n)
    # Space Complexity: O(n) for tracking added back numbers

    def __init__(self):
        self.frontier = 1  # smallest number never popped
        self.added_back = []  # min-heap of numbers added back
        self.added_back_set = set()  # for O(1) lookup

    def popSmallest(self) -> int:
        if self.added_back and self.added_back[0] < self.frontier:
            smallest = heapq.heappop(self.added_back)
            self.added_back_set.remove(smallest)
            return smallest
        else:
            result = self.frontier
            self.frontier += 1
            return result

    def addBack(self, num: int) -> None:
        # Only add back if it was previously popped (num < frontier)
        # and not already in the set
        if num < self.frontier and num not in self.added_back_set:
            heapq.heappush(self.added_back, num)
            self.added_back_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)