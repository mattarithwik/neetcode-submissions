class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_dict = Counter(s1)
        left = 0
        right = len(s1) - 1
        window_dict = Counter(s2[left:right + 1])

        while right < len(s2):
            if window_dict == char_dict:
                return True
            else:
                window_dict[s2[left]] -= 1
                if window_dict[s2[left]] == 0:
                    del window_dict[s2[left]]
                left += 1
                right += 1

                if right < len(s2):
                    window_dict[s2[right]] += 1
        return False