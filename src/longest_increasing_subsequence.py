from typing import List

class Solution:
    def explore_precedence(self, tail: int, nums: List[int], visited) -> int:
        # return the longest length
        if tail == 0:
            visited[tail] = 1
            return 1

        length = 1
        # For every potential precedence from tail
        for precedence in range(tail-1, -1, -1):
            if nums[precedence] < nums[tail]:
                if precedence in visited:
                    # no need to visit if already done before
                    length = max(length, visited[precedence] + 1)
                else:
                    length = max(length, self.explore_precedence(precedence, nums, visited) + 1)

        # Conclude the tail and cache it's max length
        visited[tail] = length
        return length


    def lengthOfLIS(self, nums: List[int]) -> int:
        # Brutal Force: Find all sequence and pick the longest
        # How many? O(n^2)
        # Optimized: add an integer to store the longest length
        # Store only the longest so far.
        # But still not improving computational time.

        if len(nums) == 1:
            return 1

        # DFS for each element as the begining
        # Mark that element as visited
        # Every iteration, find the next bigger integer and continue until the end.
        # If smaller, skip that and don't visit it.
        visited = {}
        length = 1
        for i in range(len(nums)-1, -1, -1):
            length = max(length, self.explore_precedence(i, nums, visited))
        return length


