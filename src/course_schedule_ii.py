from typing import List
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Question
        # input: Is there any pre-requiste according to the number?
        # input: Any duplicate of dependency?
        # input: Are course must be integer
        
        # Brutal force: Formulate a dependency graph. For every courses, go through the pre-requisites to find all its dependency graph.
        # Suggested solution: Mark visited notes. Formulate a dependency graph. return fail when cyclic detected. otherwise. append the course 

        # create a degree list
        degrees = [0] * numCourses
        dep_map = defaultdict(list)

        # Setup dep_map and degree
        for course, req in prerequisites:
            dep_map[req].append(course)
            degrees[course] += 1
        
        queue = deque([c for c in range(numCourses) if degrees[c] == 0])

        order = []
        while queue:
            course = queue.popleft()
            order.append(course) # take the zero degree course

            # update degree for dependency
            for req in dep_map[course]:
                degrees[req] -= 1
                if degrees[req] == 0:
                    queue.append(req) # queue to study
        
        return order if len(order) == numCourses else []



