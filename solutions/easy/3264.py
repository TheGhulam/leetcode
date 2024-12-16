#Problem 3264: Final Array State After K Multiplication Operations I

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        result = nums.copy()
        
        for _ in range(k):
            min_val = min(result)
            min_index = result.index(min_val)
            result[min_index] = min_val * multiplier
        
        return result