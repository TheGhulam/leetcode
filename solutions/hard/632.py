#Problem 632: Smallest Range Covering Elements from K Lists

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initialize minheap with first element from each list
        heap = []
        max_val = float('-inf')

        for i, lst in enumerate(nums):
            if lst:
                heappush(heap, (lst[0], i, 0))
                max_val = max(max_val, lst[0])
        
        # Initialize result range
        s = 0
        e = float('inf')

        # Until any list is exhausted
        while len(heap) == len(nums):
            min_val, list_idx, elem_idx = heappop(heap)

            # Update range if current range is smaller
            if max_val - min_val < e - s:
                s = min_val
                e = max_val
            elif max_val - min_val == e - s and min_val < s:
                s = min_val
                e = max_val
            
            # If there are more elements in current list, add next element
            if elem_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][elem_idx+1]
                heappush(heap, (next_val, list_idx, elem_idx+1))
                max_val = max(max_val, next_val)
        
        return [s, e]