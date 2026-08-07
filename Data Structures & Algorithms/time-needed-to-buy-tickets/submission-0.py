class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets_better = [0] * len(tickets)

        for i in range(len(tickets)):
            tickets_better[i] = [i, tickets[i]]

        queue = deque(tickets_better)
        time = 0

        while True:
            removed = queue.popleft()

            if removed[1] == 1:
                if removed[0] == k:
                    time += 1
                    break
            else:
                queue.append([removed[0], removed[1] - 1])
            
            time += 1

        
        return time