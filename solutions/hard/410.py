#Problem 410: Split Array Largest Sum

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(max_sum):
            # Count how many subarrays we need if we limit each subarray sum to max_sum
            count = 1  # Start with 1 subarray
            current_sum = 0
            
            for num in nums:
                # If adding this number exceeds max_sum, start a new subarray
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                else:
                    current_sum += num
                    
            return count <= k  # Can we split into k or fewer parts?
        
        l = max(nums)
        r = sum(nums)

        # Binary search for the smallest possible max sum
        res = r
        while l <= r:
            m = l + (r-l)//2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res