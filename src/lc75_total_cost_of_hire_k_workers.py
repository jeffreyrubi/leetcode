from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        workers = []
        total_cost = 0

        left_end = candidates - 1
        for i in range(candidates):
            heapq.heappush(workers, (costs[i], i))
        
        # Maximum right ended in case left_end overlaps
        right_end = max(len(costs) - candidates, left_end + 1)
        for i in range(right_end, len(costs)):
            heapq.heappush(workers, (costs[i], i))

        for i in range(k):
            cost, worker = heapq.heappop(workers)
            total_cost += cost

            # add new worker to the list if any
            if right_end - left_end > 1: 
                if worker <= left_end:
                    left_end += 1
                    heapq.heappush(workers, (costs[left_end], left_end))
                else:
                    right_end -= 1
                    heapq.heappush(workers, (costs[right_end], right_end))
        
        return total_cost
    