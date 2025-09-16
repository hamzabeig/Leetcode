class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == "(" or b=="{" or b=="[":
                stack.append(b)
            elif b == ")" and stack and stack[-1] == "(":
                stack.pop()        
            elif b == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif b == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return True if not stack else False