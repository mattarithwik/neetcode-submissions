class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            added = numbers[left] + numbers[right]
            if added == target:
                return [left + 1, right + 1]
            elif added < target:
                left += 1
            else:
                right -= 1
        return []