from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        # search for all
        while left < right:
            # update the current max_area
            x_wide = right - left
            x_height = min(height[left], height[right])
            max_area = max(max_area, x_wide * x_height)

            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_area