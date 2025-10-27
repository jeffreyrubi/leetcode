from typing import DefaultDict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = DefaultDict(lambda : 0)
        max_len = 1
        left = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            curLen = right - left + 1
            if curLen - max(freq.values()) <= k:
                max_len = max(max_len, curLen)
            else:
                freq[s[left]] -= 1
                left += 1
        return max_len