from typing import List

class Solution:
    def form_zone(self, i: int, j: int, board: List[List[str]]):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): 
            return
        
        if board[i][j] == 'X' or board[i][j] == 'C':
            return
        if board[i][j] == 'O':
            # Confirmed zone
            board[i][j] = 'C'

            # Propagate zone
            self.form_zone(i, j-1, board)
            self.form_zone(i, j+1, board)
            self.form_zone(i-1, j, board)
            self.form_zone(i+1, j, board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if len(board) < 2 or len(board[0]) < 2:
            return
        
        # Set all boundary 'O' to 'C'
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                    if board[i][j] == 'O':
                        self.form_zone(i,j, board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'C':
                    board[i][j] = 'O'