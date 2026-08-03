class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count, close_count, combo):
            if open_count == close_count == n:
                res.append("".join(combo))
                return
            
            if open_count < n:
                combo.append("(")
                backtrack(open_count + 1, close_count, combo)
                combo.pop()
            
            if close_count < open_count:
                combo.append(")")
                backtrack(open_count, close_count + 1, combo)
                combo.pop()
        
        backtrack(0, 0, [])
        
        return res