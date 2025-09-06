from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.trial(nums)

    def trial(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # reset j and k
            j = i + 1
            k = len(nums)-1

            while j < k:
                # Check
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    j = j + 1
                    while j < len(nums)-1 and nums[j] == nums[j-1]:
                        j = j + 1
                elif sum > 0:
                    k = k - 1
                    while k < len(nums)-2 and nums[k] == nums[k+1]:
                        k = k - 1
                elif sum < 0:
                    j = j + 1
                    while j < len(nums)-1 and nums[j] == nums[j-1]:
                        j = j + 1

        return result
        

    def brutal_force(self, nums: List[int]) -> List[List[int]]:
        result_list = []

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        result_list.append([nums[i], nums[j], nums[k]])

        return result_list
