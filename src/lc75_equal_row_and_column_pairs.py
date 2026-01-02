from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Brutal Force: Compare all rows with other rows and columns and all columns with other columns.
        # Time complexity: O(n^3)

        n = len(grid)
        row_count = Counter(tuple(grid[i]) for i in range(n))
        count = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += row_count[col]
        return count