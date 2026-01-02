from typing import List
from math import inf

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # brutal force: Get all combinations and check.
        # Optimize: 
        i = j = inf
        
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False
