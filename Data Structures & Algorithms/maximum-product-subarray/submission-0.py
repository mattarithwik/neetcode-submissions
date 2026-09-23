class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        
        curr_max = 1
        curr_min = 1
        
        for n in nums:
            if n < 0:
                curr_max, curr_min = curr_min, curr_max
            
            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)
            
            res = max(res, curr_max)
            
        return res