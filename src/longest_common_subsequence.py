class Solution:
    def dfs(self, text1: str, text2: str, i: int, j: int, visited) -> int:
        if (i, j) in visited:
            return visited[(i,j)]
        if i >= len(text1) or j >= len(text2):
            return 0
        if text1[i] == text2[j]:
            result = self.dfs(text1, text2, i+1, j+1, visited)
            visited[(i,j)] = 1 + result
            return visited[(i,j)]
        else:
            result = max(self.dfs(text1, text2, i, j+1, visited), self.dfs(text1, text2, i+1, j, visited))
            visited[(i,j)] = result
            return visited[(i,j)]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Brutal force:
        # For every character in text1, tries to locate it in text2 and all upcoming character onward.
        # When every match, update the length
        # Do it until all character in text 1 finished.

        # Optimization opportunities:
        # - Build a set of character for text 1. O(m)
        # - Build a heap with text2 containing only text 1 characters. O(n)
        return self.dfs(text1, text2, 0, 0, {})