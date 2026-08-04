class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        heap = [[0, k]]
        shortest_times = {}

        while heap:
            time, u= heapq.heappop(heap)
            
            if u in shortest_times:
                continue
            
            shortest_times[u] = time

            for v, w in adj[u]:
                if v not in shortest_times:
                    heapq.heappush(heap, (time + w, v))
        
        if len(shortest_times) == n:
            return max(shortest_times.values())
        else:
            return -1