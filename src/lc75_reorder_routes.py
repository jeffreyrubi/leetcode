from typing import List
from collections import deque, defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        reroute = 0
        visited = [0]*len(connections)

        # Create a from map
        from_map = defaultdict(list)
        to_map = defaultdict(list)
        for i, connection in enumerate(connections):
            frm, to = connection
            from_map[frm].append(i)
            to_map[to].append(i)
            
        city_stack = deque([0])
            
        while city_stack:
            city = city_stack.popleft()

            if city >= n:
                continue

            # Fix route that leaving the city
            for i in from_map[city]:
                if not visited[i]:
                    print(f"re-route: ({connections[i]})")
                    reroute += 1
                    city_stack.append(connections[i][1])
                    visited[i] = True
            
            # Stack route that entering the city
            for i in to_map[city]:
                if not visited[i]:
                    city_stack.append(connections[i][0])
                    visited[i] = True

        return reroute
