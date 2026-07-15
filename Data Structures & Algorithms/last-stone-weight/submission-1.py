class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            y, x = heapq.heappop_max(heap), heapq.heappop_max(heap)
            if y > x:
                heapq.heappush_max(heap, y - x)
            

        return heap[0] if heap else 0
