class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(int)

        for word in words:
            for char in word:
                count[char] += 1
        
        for char in count:
            if count[char] % len(words):
                return False
        
        return True