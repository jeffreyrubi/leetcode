from typing import List

class Solution:

    def findMatch(self, s, start, wordDict, visitedPath):
        # locate all possible match
        for word in wordDict:
            if s[start:].startswith(word):
                # Find the solution
                if start + len(word) == len(s):
                    return True
                
                # If the next start is visited, return False
                if visitedPath[start + len(word)]:
                    return False

                # Continue the search
                if self.findMatch(s, start + len(word), wordDict, visitedPath):
                    return True
                else:
                    visitedPath[start] = True

        # No match can continue the search, return False
        visitedPath[start] = True
        return False
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Clarification:
        # 1. If only one word in dict can be contain and no others, does it count is True?
        # 2. Contain any of => True. Make sense?
        # 3. Does overlap counts?
        # 4. What if the word can be separated to cover all words in word_dict but with extra unused letter. Does it count as true?

        # Brutal Force: 
        # 1. For each word in WordDict, try to locate it in 's'. If not found => false, if not at zero => continue.
        # 2. When found, slice it from 's', do another round until 's' is empty and no word in WordDict. O(w^2)
        # 
        # Optimize: DFS for possible way. Any way to the end, return True.
        # 

        # Memorize failed path start
        visitedPath = [False] * len(s)
        return self.findMatch(s, 0, wordDict, visitedPath)
    