from typing import List

class Solution:

    def expose_land_area(self, i, j, grid, visited) -> int:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] or grid[i][j] == 0:
            # out of area or already visited, return 0 area
            return 0

        visited[i][j] = True
        return 1 + self.expose_land_area(i-1, j, grid, visited) + self.expose_land_area(i+1, j, grid, visited) + self.expose_land_area(i, j-1, grid, visited) + self.expose_land_area(i, j+1, grid, visited)


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Question:
        # Confirm if corner touching is not the same island
        # A circle also considered one single island?
        
        # Brutal force: Go through all the cell, when encounter "1", add 1 to island count and perform and dfs for all four direction and mark it visited in visited matrix.
        # Continue until all cell are visited in visited matrix. Allo 

        # 1. Create a visited matrix with all 0 to tell non-visited node.
        row = len(grid)
        column = len(grid[0]) # row, column always > 0

        visited = [[False]*column for _ in range(row)]
        max_area = 0

        for i in range(row):
            for j in range(column):
                if not visited[i][j] and grid[i][j] == 1:
                    # update max_area
                    max_area = max(self.expose_land_area(i, j, grid, visited), max_area)
                    
        return max_area
