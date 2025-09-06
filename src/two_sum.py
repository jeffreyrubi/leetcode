from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.optimized(nums, target)
            
    def optimized(self, nums: List[int], target: int) -> List[int]:
        # keep updating hashmap and let the later numbr find the pair from hashmap.
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []

    def subtraction(self, nums: List[int], target: int) -> List[int]:
        top = len(nums)
        hash_map = {}

        # Complexity = n
        for i in range(top):
            hash_map[nums[i]] = i
        
        # Complexity = n
        for i in range(top-1):
            needed = target - nums[i]
            if needed in hash_map and i != hash_map[needed]:
                return [i, hash_map[needed]] 
        # Complexity: O(2n)

    def brute_force(self, nums: List[int], target: int) -> List[int]:
        # reset
        pos_0 = 0
        top = len(nums)

        # find solution
        for pos_0 in range(0, top-1):
            pos_1 = pos_0 + 1
            for pos_1 in range(pos_1, top):
                # get sum
                result = nums[pos_0] + nums[pos_1]

                if result == target:
                    return [pos_0, pos_1]
