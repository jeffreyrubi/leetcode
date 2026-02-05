from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Thoughts:
        # BFS to guarantee reaching the shortest path first.
        # O(n*m)

        # 1. Get all rotten orange in the grid to start
        # 2. while queue:
        #    2.1 Record queue size
        #    2.1 For every rotten in the queue within queue size: 
        #        2.1.1 Queue any non-rotten neighbour and mark it "x"
        #    2.2 if there are none,
        #        return 0
        #    2.3.otherwise,
        #        time_take += 1

        rotten_oranges = deque([])
        good_oranges_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten_oranges.append((r, c))
                elif grid[r][c] == 1:
                    good_oranges_count += 1
        

        # directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cycles = 0
        while rotten_oranges:
            many_in_cycle = len(rotten_oranges)
            
            for _ in range(many_in_cycle):
                # For every new rotten orange
                r, c = rotten_oranges.popleft()
                # Check each direction
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        good_oranges_count -= 1
                        rotten_oranges.append((nr, nc))
            
            # if any rotten_orange added in this cycle
            if rotten_oranges:
                cycles += 1
        return cycles if good_oranges_count == 0 else -1


            