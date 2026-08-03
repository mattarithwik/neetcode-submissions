class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        def backtrack(start: int, current_subset: list[int]):
            res.append(list(current_subset))
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
                
        backtrack(0, [])
        return res