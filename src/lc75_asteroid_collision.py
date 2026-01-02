from typing import List
from math import inf

class Solution:
    def collide(self, stack, a):
        if not stack:
            stack.append(a)
            return
        
        top = stack.pop()
        if top < 0 or (top > 0 and a > 0):
            # same polar or top is negative => don't collide
            stack.append(top)
            stack.append(a)
        elif top > 0 and top > -a:
            stack.append(top)
        elif top > 0 and top < -a:
            self.collide(stack, a)

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            self.collide(stack, a)
        return stack