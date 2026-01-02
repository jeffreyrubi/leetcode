from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Brutal Force: Tries every combination of removing zero. then count its length. Finally, compare them.
        last_zero = None
        start_of_1 = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if last_zero is not None:
                    # Need to shift
                    start_of_1 = last_zero + 1
                last_zero = i
                max_length = max(max_length, last_zero - start_of_1 + 1)
            else:
                max_length = max(max_length, i - start_of_1 + 1)
        return max_length - 1