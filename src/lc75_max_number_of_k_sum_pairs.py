from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums)-1
        ops = 0

        while left < right:
            sum = nums[left] + nums[right]
            if sum < k:
                left += 1
            elif sum > k:
                right -= 1
            else:
                left += 1
                right -= 1
                ops += 1

        return ops