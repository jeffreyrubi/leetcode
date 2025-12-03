from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column_parities = [1] * len(matrix[0])
        row_parities = [1] * len(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_parities[i] = 0
                    column_parities[j] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row_parities[i] == 0 or column_parities[j] == 0:
                    matrix[i][j] = 0
        

        