from typing import List
from collections import deque

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        cities = [0] * len(isConnected)

        # For every city
        for city in range(len(cities)):
            # Skip provinced cities
            if cities[city] == 1:
                continue

            if cities[city] == 0:
                province += 1
                
                # mark all connected city to 1
                queue = [city]
                while queue:
                    cur = queue.pop()
                    cities[cur] = 1
                    for connected in range(len(cities)):
                        if isConnected[cur][connected] == 1:
                            if cities[connected] == 0:
                                queue.append(connected)

        return province
