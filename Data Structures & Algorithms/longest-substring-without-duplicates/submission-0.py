class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in current:
                current.remove(s[left])
                left += 1
            
            current.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length