from typing import List

class Solution:
    def exploreCombinations(self, start: int, k: int, remaining: int, path: List[int], success_combinations: List[List[int]]):
        if len(path) == k and remaining == 0:
            success_combinations.append(path[:])
            return
        
        if len(path) >= k or remaining <= 0:
            return
        
        for num in range(start, 10):
            if num > remaining:
                break
            self.exploreCombinations(num + 1, k, remaining - num, path + [num], success_combinations)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        success_combinations = []
        self.exploreCombinations(1, k, n, [], success_combinations)
        return success_combinations
