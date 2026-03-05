from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # In-place solution using intermediate states:
        # 2 = was alive (1), now dead (0)
        # 3 = was dead (0), now alive (1)
        # Time: O(m*n), Space: O(1)
        
        m, n = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def count_live_neighbors(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):
                    count += 1
            return count
        
        # First pass: mark transitions
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1:
                    # Live cell dies if < 2 or > 3 neighbors
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Was alive, now dead
                else:
                    # Dead cell becomes alive if exactly 3 neighbors
                    if live_neighbors == 3:
                        board[i][j] = 3  # Was dead, now alive
        
        # Second pass: finalize states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1