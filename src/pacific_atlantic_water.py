from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Brutal Force: For every cell, find all possible cells and examine if any of them can touch. O(n^4) because every cell has 4 directions to go.
        # Optimize one: From the edge, see how water can go up the numbers. 
        #     Make a zero matrix
        #     Do it for Pacific, add 1 for all cell up or equal digit, O(m+n-1)
        #     Do it for Atlantic, add 1 for all cell up or equal digit, O(m+n-1)
        #     Loop O(m+n) and append all cell with 2.

        no_of_row = len(heights)
        no_of_col = len(heights[0])
        pacific_flow = [[0]*no_of_col for _ in range(no_of_row)]
        alantic_flow = [[0]*no_of_col for _ in range(no_of_row)]
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        final = []

        def out_of_bound(r, c):
            return r < 0 or c < 0 or r >= no_of_row or c >= no_of_col

        def flow(r, c, results, heights):
            # Visit the r,c and flow to the adjacent if it can
            if results[r][c] > 0:
                # for the first round
                return
            
            # mark visited
            results[r][c] = 1

            # attemp to all directions
            for dr, dc in directions:
                try_r = dr + r
                try_c = dc + c

                if not out_of_bound(try_r, try_c) and results[try_r][try_c] == 0 and heights[r][c] <= heights[try_r][try_c]:
                    flow(try_r, try_c, results, heights)

        # For pacific, first row
        r = 0
        for c in range(no_of_col):
            flow(r, c, pacific_flow, heights)

        c = 0
        for r in range(no_of_row):
            flow(r, c, pacific_flow, heights)

        # For alantic, first row
        r = no_of_row - 1
        for c in range(no_of_col):
            flow(r, c, alantic_flow, heights)

        c = no_of_col - 1
        for r in range(no_of_row):
            flow(r, c, alantic_flow, heights)

        # Merge result and add
        for row in range(no_of_row):
            for col in range(no_of_col):
                if pacific_flow[row][col] == alantic_flow[row][col] == 1:
                    final.append((row,col))
                    
        return final