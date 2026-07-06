class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)

        sorted_cars = sorted(cars, key=lambda x : x[0], reverse=True)
        stack = []

        for position, speed in sorted_cars:
            ttt = (target - position) / speed
            
            if stack and ttt <= stack[-1]:
                continue
            else:
                stack.append(ttt)
        
        return len(stack)