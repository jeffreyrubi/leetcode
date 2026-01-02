class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        max_count = 0
        start = 0
        end = 0

        # substring of k length doesn't exist
        if k > len(s):
            return 0

        # Get first count
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        max_count = count
        end = start + k - 1
        while end < len(s) - 1:
            if s[start] in vowels:
                count -= 1
            if s[end+1] in vowels:
                count += 1
            max_count = max(max_count, count)
            start += 1
            end += 1
        
        return max_count