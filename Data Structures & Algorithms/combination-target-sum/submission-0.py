class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, current, remaining):
            if remaining == 0:
                res.append(list(current))
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                current.append(nums[i])
                backtrack(i, current, remaining - nums[i])
                current.pop()
        
        backtrack(0, [], target)
        return res
