from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        last_segment = intervals[0]
        merged_intervals = []
        for i in range(len(intervals)):
            if intervals[i][0] <= last_segment[1]:
                last_segment[1] = max(last_segment[1], intervals[i][1])
            else:
                merged_intervals.append(last_segment)
                last_segment = intervals[i]
        merged_intervals.append(last_segment)
        return merged_intervals
