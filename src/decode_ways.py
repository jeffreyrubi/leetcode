class Solution:
    def numDecodings(self, s: str) -> int:
        dp_1 = dp_2 = 1

        for i in range(len(s)-1, -1, -1):
            temp = 0
            if s[i] in "123456789":
                temp += dp_1
            if i < len(s)-1 and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                temp += dp_2

            # shift position
            dp_2 = dp_1
            dp_1 = temp

        return dp_1