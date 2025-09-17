from typing import List

class Solution:
    def land(self, i: int, j: int, grid: List[List[str]]):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == '1':
            grid[i][j] = 'C'
        elif grid[i][j] == 'C' or grid[i][j] == '0':
            return
        
        self.land(i-1, j, grid)
        self.land(i+1, j, grid)
        self.land(i, j-1, grid)
        self.land(i, j+1, grid)


    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.land(i, j, grid)
                    num_of_island += 1
        
        return num_of_island


    