from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brutal force: For every elment i, loop for j to find the next higher temperature day. O(n ^ 2)
        # My proposal:
        # Intuitive:
        # visit i for every element, Have a minheap to keep track of the unsolved day and their position.
        # if i temperature > heap[0] => put i - heap[0].val to result array. pop the min element.
        # do this until no other heap[0] < i temperature.
        # continue to move.
        
        results = [0] * len(temperatures) # default to unresolved
        temp_stack = [] # store the un-resolved index
        for i in range(len(temperatures)):
            while len(temp_stack) > 0 and temperatures[i] > temperatures[temp_stack[-1]]:
                pos = temp_stack.pop()
                results[pos] = i - pos
            temp_stack.append(i)

        # Edge cases
        # 1. one element, covered by default
        # 2. all unresolved, covered by default
        return results