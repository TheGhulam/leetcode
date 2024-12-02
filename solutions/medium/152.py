#Problem 152: Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        curr_max = curr_min = result = nums[0]
    
        for num in nums[1:]:
            temp_max = curr_max
            
            # For each number, we need to compare:
            # 1. The number itself
            # 2. Number * current maximum (could be good if both are positive or both negative)
            # 3. Number * current minimum (could be good if both are negative)
            curr_max = max(num, temp_max * num, curr_min * num)
            curr_min = min(num, temp_max * num, curr_min * num)
            
            result = max(result, curr_max)
        
        return result