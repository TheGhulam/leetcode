#Problem 1760: Minimum Limit of Balls in a Bag

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1  # Minimum possible value
        r = max(nums)  # Maximum possible value

        def canAchieve(target):
            # Count operations needed to get all nums <= target
            o = 0
            for n in nums:
                o += (n-1) // target
            return o <= maxOperations
        
        res = r
        while l <= r:
            mid = (l+r)//2
            if canAchieve(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res