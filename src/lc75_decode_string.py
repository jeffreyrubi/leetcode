from typing import Tuple

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
                continue

            # ']'
            word = ""
            one_char = stack.pop()
            while one_char != "[":
                word = one_char + word
                one_char = stack.pop()
            
            # '['
            num = ""
            one_digit = stack.pop()
            while one_digit.isdigit():
                num = one_digit + num
                if stack:
                   one_digit = stack.pop()
                   if not one_digit.isdigit():
                       stack.append(one_digit)
                else:
                    break
            stack.append(word * int(num))

        return ''.join(stack) 
            






    