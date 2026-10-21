class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ""

        curr = strs[0][0]
        i = 0

        while True:
            for word in strs:
                if i >= len(word) or word[i] != curr:
                    return strs[0][0:i]
            i += 1
            if i >= len(strs[0]):
                return strs[0][0:i]
            curr = strs[0][i]
        
        return strs[0][0:i]