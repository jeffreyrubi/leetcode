from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Use prefix and suffix products without division
        # Time: O(n), Space: O(1) extra (output array doesn't count)
        
        n = len(nums)
        result = [1] * n
        
        # First pass: compute prefix products (product of all elements to the left)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Second pass: multiply by suffix products (product of all elements to the right)
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result