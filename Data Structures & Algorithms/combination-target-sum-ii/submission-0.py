class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, current, remaining):
            if remaining == 0:
                res.append(list(current))
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return res