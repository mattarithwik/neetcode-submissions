class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        counts = Counter(hand)
        hand.sort()
        groups = 0

        for i in range(n):
            card = hand[i]
            if counts[card] == 0:
                continue

            for num in range(card, card + groupSize):
                if counts[num] > 0:
                    counts[num] -= 1
                else:
                    return False
            groups += 1
            if groups == n // groupSize:
                return True
        
        return True



