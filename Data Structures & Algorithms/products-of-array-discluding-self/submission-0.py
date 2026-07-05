class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        left_running_sum = 1
        for i in range(n):
            output[i] *= left_running_sum
            left_running_sum *= nums[i]

        right_running_sum = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_running_sum
            right_running_sum *= nums[i]
        
        return output