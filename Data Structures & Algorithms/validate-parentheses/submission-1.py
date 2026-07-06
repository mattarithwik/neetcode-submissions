class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        mapping = {")": "(", "}" : "{", "]" : "["}

        for c in s:
            if c in mapping:
                if stack and stack.pop() == mapping[c]:
                    continue
                else:
                    return False
            stack.append(c)
        
        return len(stack) == 0