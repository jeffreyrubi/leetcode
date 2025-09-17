from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.trial(nums, target)
    
    def trial(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        k_val = nums[0]
        k_minus_1_val = nums[-1]
        max_m = len(nums) - 1
        m = int(max_m/2)

    
        while True:
            # Case 0: Find it
            if nums[m] == target:
                return m

            # Case 0.1: Not find it
            if max_m > 1 and (m == 0 or m == max_m):
                return -1
            if k_minus_1_val < target < k_val:
                return -1
            if max_m == 0 and m == 0:
                return -1
                        
            # Case 0.2: Edge case
            if max_m == 1:
                if nums[0] == target:
                    return 0
                if nums[1] == target:
                    return 1
                return -1
            
            # Case 1: m >= k
            if nums[m] >= k_val:
                if k_val <= target < nums[m]:
                    # limit the search to below m
                    max_m = m
                    # Target at left hand side
                    m = min(int(m/2), m-1)
                else:
                    # Target at right hand side
                    m = max(int((max_m - m)/2), 1) + m
                continue
            
            # Case 2: m <= k-1
            if nums[m] <= k_minus_1_val:
                if nums[m] < target <= k_minus_1_val:
                    # Traget at right hand side
                    m = max(int((max_m - m)/2), 1) + m
                else:
                    max_m = m
                    # Target at left hand side
                    m = min(int(m/2), m-1)

        

        