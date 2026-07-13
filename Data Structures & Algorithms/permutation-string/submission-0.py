class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_dict = Counter(s1)
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            sub = s2[left:right+1]
            if Counter(sub) == char_dict:
                return True
            else:
                left += 1
                right += 1
        return False