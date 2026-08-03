class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        
        def backtrack(current_permutation: list[int]):
            if len(current_permutation) == len(nums):
                res.append(list(current_permutation))
                return
            
            for i in range(len(nums)):
                if nums[i] not in used:
                    current_permutation.append(nums[i])
                    used.add(nums[i])
                    backtrack(current_permutation)
                    current_permutation.pop()
                    used.remove(nums[i])
                
        backtrack([])
        return res