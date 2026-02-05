from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        visiting = [0]

        while visiting:
            cur = visiting.pop() 
            for i in rooms[cur]:
                if not i in visited:
                    visited.add(i)
                    visiting.append(i)
            if len(visited) == len(rooms):
                return True

        return False
