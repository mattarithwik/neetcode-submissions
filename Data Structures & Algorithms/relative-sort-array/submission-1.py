class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for num in arr2:
            for _ in range(count[num]):
                res.append(num)
            del count[num]
        
        leftover = sorted(count.keys())
        for num in leftover:
            res.extend([num] * count[num])

        return res