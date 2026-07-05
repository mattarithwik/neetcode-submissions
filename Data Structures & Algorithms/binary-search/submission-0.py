class Solution:
    def search(self, nums: List[int], target: int) -> int:
       return self.binSearch(nums, 0, len(nums) - 1, target)

    def binSearch(self, nums, start, end, target):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binSearch(nums, start, mid - 1, target)
        else:
            return self.binSearch(nums, mid + 1, end, target)