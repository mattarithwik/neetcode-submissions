class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)

        max_odd = 0
        min_even = float("inf")

        for freq in counts.values():
            if freq % 2 == 0:
                min_even = min(min_even, freq)
            else:
                max_odd = max(max_odd, freq)

        return max_odd - min_even
