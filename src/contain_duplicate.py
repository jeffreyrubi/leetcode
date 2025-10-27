from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # question:
        # 1. is the input always contain some values? what to return if empty?
        # 2. is it comply with the integer rule?

        # Brutal Force: go through every elements and count it's exist. if anyone duplicate, immediate return True. 
        #               otherwise, return false

        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False

