from typing import DefaultDict, List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      # Question to ask
      # 1. Input: depend on itself?
      # 2. Input: does the number of courses fit in memory?
      # 3. Input: What if pre-requisite fall outside numCourses?

      # Procedure
      # Build the dependency tree as dictionary with key(numCourse): value(all dependencies): O(dep)
      # Traverse the numCourses: if no dependency, remove it from the dictionary and remove 
      # Do this until all non-depending node is removed.
      # dependency is not empty -> There are cycle and return False

      # dep_map[i] is the preq of course i 
      dep_map = [[] for _ in range(numCourses)]
      for course, prep in prerequisites:
         dep_map[course].append(prep)
      
      # mark node status
      # 0 = not visited, 1 = visiting, 2 = fine
      visited = [0] * numCourses

      def dfs(course, dep_map) -> bool:
        # Traverse the tree and return false if cyclic happens
        if visited[course] == 1:
          # cyclic detected
          return False
        
        if visited[course] == 2:
          # fine
          return True
        
        # Mark visiting
        visited[course] = 1

        # End Case: course has no dep_map, report no cyclic downstream
        if len(dep_map[course]) == 0:
          visited[course] = 2
          return True

        # Continue bfs
        for neighbour in dep_map[course]:
          if not dfs(neighbour, dep_map):
            return False 
        
        # All prequisite can finish
        visited[course] = 2
        return True
      
      for course in range(numCourses):
        if not dfs(course, dep_map):
           return False
      
      return True
        