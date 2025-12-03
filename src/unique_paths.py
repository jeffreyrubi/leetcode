class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        canvas = [[0]*(n+1) for _ in range(m+1)]
        
        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                canvas[i][j] = (canvas[i][j+1] + canvas[i+1][j]) or 1
        return canvas[0][0]