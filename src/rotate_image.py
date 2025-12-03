from typing import List

class Solution:
    def rotate_one_piece(self, matrix: List[List[int]], i: int, j: int) -> None:
        last = len(matrix) - 1
        
        # Step 1:
        temp = matrix[j][last-i]
        matrix[j][last-i] = matrix[i][j]
        # print(f"move [{i},{j}] to [{j},{last-i}]")

        # Step 2:
        temp2 = matrix[last-i][last-j]
        matrix[last-i][last-j] = temp
        # print(f"move [{j},{last-i}] to [{last-i},{last-j}]")

        # Step 3:
        temp = matrix[last-j][i]
        matrix[last-j][i] = temp2
        # print(f"move [{last-i},{last-j}] to [{last-j},{i}]")

        # Step 4:
        matrix[i][j] = temp
        # print(f"move [{last-j},{i}] to [{i},{j}]")

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
                  
        for i in range(int(length/2)):
            for j in range(i, length-i-1):
                self.rotate_one_piece(matrix, i, j)
        
        
