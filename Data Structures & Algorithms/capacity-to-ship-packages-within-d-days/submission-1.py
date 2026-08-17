class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right

        def canShip(capacity):
            ships = 1
            currCapacity = capacity
            for weight in weights:
                if currCapacity - weight < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCapacity = capacity

                currCapacity -= weight
            return True

        while left <= right:
            capacity = (left + right) // 2
            if canShip(capacity):
                res = min(res, capacity)
                right = capacity - 1
            else:
                left = capacity + 1

        return res
