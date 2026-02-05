from typing import List
from math import inf

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Brutal Force: Try all combinations of arrows => O(n^n-1)
        # Optimal: Sort all balloon in left assending order. Try to shoot right most that can cover the left most balloon. (O(n))
        # Sort all the points by x start
        points.sort(key=lambda x: x[0])
        
        # Always make an arrow for the first balloon
        cur_start = -inf
        cur_end = -inf
        arrow = 0
        
        # Start merging points until end
        for point in points:
            if point[0] > cur_end:
                # no overlap
                arrow += 1
                cur_start = point[0]
                cur_end = point[1]
            else:
                # Overlap, merge
                cur_start = point[0]
                cur_end = min(cur_end, point[1])
        
        return arrow