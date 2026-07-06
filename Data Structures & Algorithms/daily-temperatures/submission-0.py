class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                pop_i, pop_temp = stack.pop()
                res[pop_i] = i - pop_i
            stack.append((i, temp))

        return res