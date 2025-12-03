from typing import List
import math

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        remove_count = 0
        last_pointer = -math.inf
        for pair in intervals:
            if pair[0] >= last_pointer:
                last_pointer = pair[1]
            else:
                remove_count += 1
        return remove_count