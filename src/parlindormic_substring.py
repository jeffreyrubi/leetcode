class Solution:
    def countSubstrings(self, s: str) -> int:
        # Brutal force: For every character, get all possible substring. O(n^4). Test if the string is parlindormic.
        # Optimize: For every character and in between, extend at both end and get every parlindormic substring until it failed.
        
        n = len(s)
        p_substrs = []

        def get_parlindormic_from_pivot(s, pivot, p_substrs):
            delta = 0
            while pivot - delta >= 0 and pivot + delta < n:
                if s[pivot - delta] == s[pivot + delta]:
                    p_substrs.append(s[pivot - delta:pivot + delta + 1])
                else:
                    break
                delta += 1
        
        def get_parlindormic_from_mid(s, mid, p_substrs):
            delta = 0
            while mid - delta >= 0 and mid + 1 + delta < n:
                if s[mid - delta] == s[mid + 1 + delta]:
                    p_substrs.append(s[mid - delta:mid + 1 + delta + 1])
                else:
                    break
                delta += 1
            

        for i in range(n):
            get_parlindormic_from_pivot(s, i, p_substrs)
            get_parlindormic_from_mid(s, i, p_substrs)

        return len(p_substrs)