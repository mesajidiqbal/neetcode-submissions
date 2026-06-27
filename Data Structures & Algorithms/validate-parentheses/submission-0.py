class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for c in s:
            if c in paren_map.keys():
                if stack and stack[-1] == paren_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        