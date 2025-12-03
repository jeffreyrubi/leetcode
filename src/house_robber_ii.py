from typing import List

class Solution:
    def rob_dp(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_dp(nums[1:]), self.rob_dp(nums[:-1]))
        