from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0

        for n in num_set:
            if n-1 not in num_set:
                y = n + 1
                cur_count = 1
                while y in num_set:
                    y += 1
                    cur_count += 1
                max_seq = max(cur_count, max_seq)
        return max_seq