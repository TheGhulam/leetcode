#Problem 164: Maximum Gap

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        
        minv, maxv = min(nums), max(nums)
        if minv == maxv: return 0

        n = len(nums)
        bucketsize = max(1, (maxv - minv) // (n-1)) #Minimum possible gap
        buckets = [[] for _ in range((maxv - minv) // bucketsize + 1)] # ceil((maxv - minv) / bucketsize)

        for n in nums:
            if n == maxv:
                idx = len(buckets) - 1
            else:
                idx = (n - minv) // bucketsize
            buckets[idx].append(n)

        #Remove empty buckets
        buckets = [b for b in buckets if b]

        #Find max gap
        maxgap = 0
        prevmax = max(buckets[0])

        for i in range(1, len(buckets)):
            currmin = min(buckets[i])
            maxgap = max(maxgap, currmin - prevmax)
            prevmax = max(buckets[i])

        return maxgap