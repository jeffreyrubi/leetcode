from typing import List

class Solution:
    def exploreSubtarget(self, candidates, subtarget, path, success_combinations):
        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate == subtarget:
                # Solution is found
                success_combinations.append(path + [candidate])
            
            if candidate < subtarget:
                # Subtarget is achieved
                self.exploreSubtarget(candidates[i:], subtarget-candidate, path + [candidate], success_combinations)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Question:
        # What to return if target = 0? 
        # What if there so many candidates to explore? 
        # Does the size of the answer fit the memory or there is a max number of combination required?
        
        # Brutal Force:
        # Find the max number of number that can be used to sum up the target. Make the array with all those numbers.
        # Make all combinations of that array and then examine their sum to pick those add up to seven. 
        # Optimized:
        # 1. DFS from target. 
        # 2. For each candidate that smaller than it. Subtract it and continue the next iteration until it gets to zero.
        # 3. If not, failed the path. Mark that such number has no way to find a combination for other search to skip.
        # if return True, append it to the success_combination
        # if return False, mark failed_subtarget. 

        visited_subtarget = set()
        success_combinations = []
        self.exploreSubtarget(candidates, target, [], success_combinations)
        return success_combinations

        
        