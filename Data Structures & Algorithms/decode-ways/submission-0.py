class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # prev2 corresponds to dp[i-2], prev1 corresponds to dp[i-1]
        prev2 = 1  # dp[0]: empty string
        prev1 = 1  # dp[1]: valid first character

        for i in range(1, len(s)):
            current = 0

            # 1. Single digit decode: s[i]
            if s[i] != "0":
                current += prev1

            # 2. Two-digit decode: s[i-1:i+1]
            two_digit = int(s[i - 1 : i + 1])
            if 10 <= two_digit <= 26:
                current += prev2

            # If current is 0, string cannot be decoded further
            if current == 0:
                return 0

            prev2, prev1 = prev1, current

        return prev1