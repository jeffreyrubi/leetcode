from typing import List

class Solution:
    def dfs(self, board, path, i, j, word, c) -> bool:
        if (i, j) in path or i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[c]:
            return False

        if c == len(word) -1:
            # Get all word
            return True

        path.add((i, j))
        
        if self.dfs(board, path, i, j+1, word, c+1):
            return True
        if self.dfs(board, path, i, j-1, word, c+1):
            return True
        if self.dfs(board, path, i+1, j, word, c+1):
            return True
        if self.dfs(board, path, i-1, j, word, c+1):
            return True
        path.remove((i, j))
        return False
               

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                path = set()
                if self.dfs(board, path, i, j, word, 0):
                    return True
        return False