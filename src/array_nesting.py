from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [0] * len(nums)
        longest_length = 1

        for i in range(len(nums)):
            sublist_length = 0
            while not visited[i]:
                visited[i] = 1 # mark visited
                i = nums[i]
                sublist_length += 1
            longest_length = max(sublist_length, longest_length)

        return longest_length
