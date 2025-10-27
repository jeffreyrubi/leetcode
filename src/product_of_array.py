from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        results = [1]*n

        for i in range(n):
            results[i] *= prefix
            prefix *= nums[i]
        for i in range(n-1, -1, -1):
            results[i] *= suffix
            suffix *= nums[i]
        return results



        

