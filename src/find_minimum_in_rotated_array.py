from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        
        while left <= right:
            m = int((right - left) / 2) + left

            if nums[m-1] > nums[m]:
                return nums[m]
            elif nums[m] < nums[right]:
                right = m - 1
            else:
                left = m + 1
            






        
