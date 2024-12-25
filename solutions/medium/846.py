#Problem 846: Hand of Straights

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        counts = Counter(hand)
        sorted_counts = sorted(counts.keys())

        # Treating each card as potential start of group
        for c in sorted_counts:
            if counts[c] == 0:
                continue
            
            freq = counts[c]
            for num in range(c, c + groupSize):
                if counts[num] < freq:
                    return False
                counts[num] -= freq
            
        return True