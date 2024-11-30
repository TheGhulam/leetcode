#Problem 179: Largest Number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
    
        def compare(n1, n2):
            # If n1+n2 is greater than n2+n1, n1 should come first
            if n1 + n2 > n2 + n1:
                return -1
            return 1
        
        # Sort using custom comparison
        nums.sort(key=functools.cmp_to_key(compare))
        
        # Handle edge case of all zeros
        if nums[0] == '0':
            return '0'
        
        return ''.join(nums)