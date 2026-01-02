from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Brutal Force: try every combination of flipping 0 to 1, evaluate the max 1.
        # Time complexity: O(n^(n-k)) where n is the number of 0
          
        # Find out all zeros
        zeros_at = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_at.append(i)

        if len(zeros_at) <= k:
            return len(nums)

        # Iterate first sliding window
        max_length = 0
        
        # Iterate a sliding window of size k
        for w in range(0, len(zeros_at)-k+1):
            start_of_1 = zeros_at[w-1] + 1 if w > 0 else 0
            end_of_1 = zeros_at[w+k] - 1 if (w + k) < len(zeros_at) else len(nums)-1
            max_length = max(end_of_1 - start_of_1 + 1, max_length)

        return max_length