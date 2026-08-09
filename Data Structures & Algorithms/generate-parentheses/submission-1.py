class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()

        def backtrack(openNum, closeNum, curr):
            if openNum == n and closeNum == n:
                res.append(curr)
                return

            if openNum < n:
                backtrack(openNum + 1, closeNum, curr + "(")
               
            if closeNum < openNum:
                backtrack(openNum, closeNum + 1, curr + ")")


        backtrack(0, 0, "")
        return res