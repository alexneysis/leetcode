class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
    
        for v in s:
            if v in brackets:
                if stack and brackets[v] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(v)
    
        return not stack