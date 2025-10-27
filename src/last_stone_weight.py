from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Find largest odd number
        sorted_stones = []
        for stone in stones:
            heapq.heappush(sorted_stones, -stone)

        while len(sorted_stones) > 1:
            stone_1 = (heapq.heappop(sorted_stones))
            stone_2 = (heapq.heappop(sorted_stones))
            heapq.heappush(sorted_stones, -abs(stone_1-stone_2))

        return -heapq.heappop(sorted_stones) if len(sorted_stones) > 0 else 0

            
