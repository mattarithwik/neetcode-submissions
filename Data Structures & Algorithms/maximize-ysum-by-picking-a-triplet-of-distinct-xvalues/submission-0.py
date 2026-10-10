class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        new_y = []

        for i, num in enumerate(y):
            new_y.append((num, i))

        res_y = sorted(new_y, key=lambda x: -x[0])

        res = []
        i = 0

        while len(res) < 3 and i < len(res_y):
            index = res_y[i][1]
            num = res_y[i][0]
            flag = False
            for val in res:
                j= val[0]
                if x[j] == x[index]:
                    flag = True
                    break
            if flag:
                i += 1
                continue
            res.append((index, num))
            i += 1
        
        if len(res) < 3:
            return -1

        ret = 0
        for index, num in res:
            ret += num

        return ret

