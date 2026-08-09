class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque([nums[0]])
        dec = deque([nums[0]])
        res = 1
        left = 0

        for right in range(1, len(nums)):
            while inc and inc[-1] > nums[right]:
                inc.pop()
            while dec and dec[-1] < nums[right]:
                dec.pop()

            inc.append(nums[right])
            dec.append(nums[right])
            if dec[0] - inc[0] > limit:
                if dec[0] == nums[left]:
                    dec.popleft()
                if inc[0] == nums[left]:
                    inc.popleft()
                left += 1

        return len(nums) - left