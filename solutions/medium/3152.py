#Problem 3152: Special Array II

# Naive solution O(N*Q)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def isSpecial(nums, i, j):
            parity = nums[i] % 2
            for idx in range(i+1, j+1):
                p = nums[idx] % 2
                if p == parity:
                    return False
                else:
                    parity = p
            return True
    

        res = []
        for q in queries:
            res.append(isSpecial(nums, q[0], q[1]))
        return res
    
# Optimized solution O(N+Q)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        # Store positions where adjacent elements have same parity
        same_parity = [0] * (n-1) # -1 because of pairs

        for i in range(n-1):
            if nums[i] % 2 == nums[i+1] % 2:
                same_parity[i] = 1
            
        # Prefix sum array for quick range queries
        prefix = [0] * n
        if n > 1:
            prefix[1] = same_parity[0]
            for i in range(2, n):
                prefix[i] = prefix[i-1] + same_parity[i-1]
        
        # Process queries
        res = []
        for i, j in queries:
            if i == j:
                res.append(True)
                continue
            
            count = prefix[j] - (prefix[i] if i > 0 else 0)
            res.append(count == 0)
        return res