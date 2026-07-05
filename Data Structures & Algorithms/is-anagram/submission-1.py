class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = list(s)
        charsOther = list(t)

        if sorted(chars) == sorted(charsOther):
            return True
        return False