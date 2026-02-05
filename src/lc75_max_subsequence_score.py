from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Concept
        # For each minimum, get the largest scores
        # Update the max_score

        pairs = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        # sort by nums2
        pairs.sort(key = lambda p: p[1], reverse=True)

        subsequence = []
        subsequence_sum = 0
        max_sum = 0

        for num1, num2 in pairs:
            heapq.heappush(subsequence, num1)
            subsequence_sum += num1

            if len(subsequence) > k:
                subsequence_sum -= heapq.heappop(subsequence)

            if len(subsequence) == k:
                max_sum = max(max_sum, subsequence_sum * num2)

        return max_sum


            