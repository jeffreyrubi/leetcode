from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Question:
        c = Counter(nums)

        return [a for a, num in c.most_common(k)]


