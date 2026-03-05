class Solution:
    def simplifyPath(self, path: str) -> str:
        # idea: ".." = pop (go up), "." = ignore, "" = ignore (multiple slashes)
        # Time: O(n), Space: O(n)
        
        stack = []
        parts = path.split("/")
        
        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)
        
        return "/" + "/".join(stack)