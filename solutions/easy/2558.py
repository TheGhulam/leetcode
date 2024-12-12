#Problem 2558: Take Gifts From the Richest Pile

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            m = -heapq.heappop(gifts)
            heapq.heappush(gifts, -math.floor(math.sqrt(m)))

        return -sum(gifts)