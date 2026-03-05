from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Approach: Sort descending, find largest h where citations[h-1] >= h
        # Time: O(n log n), Space: O(1)
        
        citations.sort(reverse=True)
        h = 0
        
        for i, c in enumerate(citations):
            # i+1 papers have been seen so far
            # If current paper has at least i+1 citations, h-index is at least i+1
            if c >= i + 1:
                h = i + 1
            else:
                break
        
        return h