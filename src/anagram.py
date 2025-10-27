from typing import DefaultDict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Question
        # 1. repeat character count?
        # 2. Upper lower case?
        # sorted => O(nlog(n))

        if len(s) != len(t):
            return False

        s_count = DefaultDict(lambda: 0)
        t_count = DefaultDict(lambda: 0)

        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1

        return s_count == t_count