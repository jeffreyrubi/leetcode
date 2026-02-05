from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # Create an adjacent list for random and bi-directional traversal
        adj = defaultdict(dict)

        for equation, value in zip(equations, values):
            up, down = equation
            adj[up][down] = value
            adj[down][up] = 1 / value
        
        def dfs(query, visited) -> float:
            nonlocal adj 
            up, down = query

            if up not in adj or down not in adj:
                return -1.0

            visited.add(up) # don't explore any 'up' down the path
            for kd, kv in adj[up].items():
                if kd == down:
                    return kv
                elif kd in visited:
                    continue
                else:
                    result = kv * dfs([kd, down], visited)
                    if result >= 0.0:
                        return result
                    # otherwise, look for other path
            return -1
        
        return [dfs(query, set()) for query in queries]
