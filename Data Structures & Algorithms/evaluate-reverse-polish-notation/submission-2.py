class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 + num2)
            elif c == '/':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2 / num1))
            elif c == '*':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 * num2)
            elif c == '-':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            else:
                stack.append(int(c))
        
        return stack[0]