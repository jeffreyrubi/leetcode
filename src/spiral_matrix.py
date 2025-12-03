from typing import List

class Solution:
    def left(self, matrix: List[List[int]], origin_i: int, path: List[int]) -> bool:
        cols = len(matrix[0])
        if cols > 1 and origin_i > cols-1-origin_i:
            # no more left to consume
            return False

        path.extend(matrix[origin_i][origin_i:cols-origin_i])
        return True
    
    def down(self, matrix: List[List[int]], origin_i: int, path: List[int]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if origin_i >= rows//2:
            # no more down to consume
            return False
        
        path.extend([matrix[i][cols-1-origin_i] for i in range(origin_i+1,rows-origin_i)])
        return True
    
    def right(self, matrix: List[List[int]], origin_i: int, path: List[int]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if cols-1 <= origin_i * 2:
            return False
        path.extend(matrix[rows-1-origin_i][origin_i:-1-origin_i][::-1])
        return True
    
    def up(self, matrix: List[List[int]], origin_i: int, path: List[int]) -> bool:
        rows = len(matrix)
        if (origin_i+1)*2 >= rows:
            return False
        path.extend([matrix[i][origin_i] for i in range(rows-2-origin_i, origin_i, -1)])
        return True
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = []
        for i in range(len(matrix)):
            if not self.left(matrix, i, path):
                break
            if not self.down(matrix, i, path):
                break
            if not self.right(matrix, i, path):
                break
            if not self.up(matrix, i, path):
                break
        return path