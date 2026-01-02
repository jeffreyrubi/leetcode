class Solution:
    def reverseWords(self, s: str) -> str:
        # Brutal Force: put all words in a list, then, iterate from the end.
        # Optimize: reverse the whole string and then, reverse word by word.

        # Reverse the whole string
        words = s.split()
        return ' '.join(words[::-1])
