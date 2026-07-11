class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]
        
        total = 0

        while left < right:
            if height[left] <= height[right]:
                left += 1
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
            else:
                right -= 1
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
        
        return total