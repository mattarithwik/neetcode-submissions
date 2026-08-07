class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr] = nums[i]
                curr += 1
        
        for i in range(curr, len(nums)):
            nums[i] = 0