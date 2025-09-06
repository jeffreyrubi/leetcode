class Solution:
    def isValid(self, s: str) -> bool:
        return self.improved(s)

    def improved(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            if c == ']' or c == '}' or c == ')':
                if len(stack) == 0:
                    return False
                c2 = stack.pop()
                if c == ']' and c2 == '[':
                    continue
                elif c == '}' and c2 == '{':
                    continue
                elif c == ')' and c2 == '(':
                    continue
                else:
                    return False
        if len(stack) != 0:
            return False
        return True

    def trial(self, s: str) -> bool:
        parenthesis = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for c in s:
            if c in parenthesis:
                stack.append(parenthesis[c])
            if c in parenthesis.values():
                nearest = stack.pop()
                if c != nearest:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True