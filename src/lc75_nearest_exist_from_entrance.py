from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # BFS for shortest path - O(m*n) time, O(m*n) space
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        maze[entrance[0]][entrance[1]] = '+'  # Mark visited by modifying in-place
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, steps = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and walls
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    # Check if it's an exit (on border and not entrance)
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1
                    
                    # Mark visited and add to queue
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))
        
        return -1