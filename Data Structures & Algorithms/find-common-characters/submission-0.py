class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words:
            curr = Counter(word)
            for char in count:
                count[char] = min(count[char], curr[char])
                    
        res = []
        for char in count:
            for i in range(count[char]):
                res.append(char)
        
        return res
            