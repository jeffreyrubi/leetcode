from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding window approach
        # Idea: Expand right to increase sum, shrink left when sum >= target
        # Time: O(n), Space: O(1)
        
        n = len(nums)
        min_len = float("inf")
        left = 0
        current_sum = 0
        
        for right in range(n):
            current_sum += nums[right]
            
            # Shrink window while sum is still >= target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float("inf") else 0