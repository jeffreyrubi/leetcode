from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r
        while l <= r:            
            k = (r+l)//2 # pick a speed

            # Check if it can finished before h
            hours = 0
            for p in piles:
                hours += math.ceil(p/k) # consume all bananas

            if hours > h:
                # cannot finished => search a bigger k
                l = k + 1
            else:
                # can finish => search for a smaller k
                r = k - 1
                res = min(res, k) # update can finished speed

        return res
