#Problem 2054: Two Best Non-Overlapping Events

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)

        dp = [0] * n # Max value seen so far for each end time
        dp[0] = events[0][2]
        for i in range(1, n):
            dp[i] = max(dp[i-1], events[i][2])
        
        res = dp[-1] # Best single event value

        # For each event as second event
        for i in range(n): 
            s, e, v = events[i]

            # Binary search for last event that ends before this one starts
            l, r = 0, i
            while l < r:
                m = (l+r)//2
                if events[m][1] < s:
                    l = m + 1
                else:
                    r = m
            
            if l > 0: # Found valid element
                res = max(res, v + dp[l-1])
            
        return res