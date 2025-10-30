class Solution:


    def longestPalindrome(self, s: str) -> str:
        # Brutal force: for every character, get all string combinations. O(n^2)
        # Compare every pair and remove the parent if it contains the child. O(n^2)
        
        # Optimized:
        # 0. Setup a longest string result.
        # 1. From 0.5 to n-0.5, expand left and right half step, to look for longest parlindrome. update result if it gets longer.
        # 2. From 1 to n-1, expand left and right in 1 step, to look for longest parlinrome. update result if it gets longer.

        if len(s) <= 1:
            return s

        def find_palindrome_from_mid(s: str, mid: int) -> str:
            # return the longest palindrome.
            # default is s[mid]
            delta = 0
            left = mid - delta
            right = mid + delta
            result = s[mid]
            while left >= 0 and right <= (n - 1):
                if s[left] != s[right]:
                    break
                result = s[left:right+1]
                delta += 1
                left = mid - delta
                right = mid + delta

            return result
        
        def find_palindrome_at_half(s: str, half: int) -> str:
            # return the longest palindrome.
            # default is s[mid]
            delta = 0
            left = half - delta
            right = half + 1 + delta
            result = ""
            while left >= 0 and right <= (n - 1):
                if s[left] != s[right]:
                    break
                result = s[left:right+1]
                delta += 1
                left = half - delta
                right = half + 1 + delta

            return result

        longest_str = ""
        n = len(s)

        for i in range(0, n-1, 1):
            par = find_palindrome_at_half(s, i)
            longest_str = par if len(par) > len(longest_str) else longest_str
            par = find_palindrome_from_mid(s, i)
            longest_str = par if len(par) > len(longest_str) else longest_str
            # with centre (0, 1, 2), (0, 1, 2, 3, 4), 
            # without centre (0,1), (0, 1, 2, 3) 
        
        return longest_str