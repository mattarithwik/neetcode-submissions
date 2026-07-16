class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            if len(heap) < k:
                heapq.heappush_max(heap, (dist, point))
            elif dist < heap[0][0]:
                heapq.heapreplace_max(heap, (dist, point))
        
        for i, element in enumerate(heap):
            heap[i] = element[1]
        return heap