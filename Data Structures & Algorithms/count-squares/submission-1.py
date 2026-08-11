class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point[0], point[1]
        
        for (cx, cy), count in self.points.items():
            dx = abs(cx - px)
            dy = abs(cy - py)
            
            if dx == 0 or dx != dy:
                continue
                
            corner1 = (px, cy)
            corner2 = (cx, py)
            
            if corner1 in self.points and corner2 in self.points:
                res += count * self.points[corner1] * self.points[corner2]
        
        return res