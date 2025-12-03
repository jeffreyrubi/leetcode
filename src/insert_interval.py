from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged_intervals = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                merged_intervals.append(newInterval)
                return merged_intervals + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                merged_intervals.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        merged_intervals.append(newInterval)
        return merged_intervals
        