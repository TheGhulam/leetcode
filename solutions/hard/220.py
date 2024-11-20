#Problem 220: Contains Duplicate iii

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff < 0 or valueDiff < 0:
            return False
        
        # Each bucket will have range of valueDiff + 1
        # This ensures numbers that could satisfy the valueDiff condition will either be in the same bucket or adjacent buckets
        bucket = {}
        w = valueDiff + 1
        
        for i in range(len(nums)):
            # Get bucket index for current number
            # We add an offset to handle negative numbers
            bucket_id = nums[i] // w
            
            # Check if there's already a number in the same bucket
            # If yes, then difference is automatically <= valueDiff
            if bucket_id in bucket:
                return True
                
            # Check adjacent buckets
            # Only need to check bucket_id-1 and bucket_id+1
            # as other buckets would have difference > valueDiff
            if (bucket_id - 1) in bucket and abs(nums[i] - bucket[bucket_id - 1]) < w:
                return True
            if (bucket_id + 1) in bucket and abs(nums[i] - bucket[bucket_id + 1]) < w:
                return True
                
            # Add current number to its bucket
            bucket[bucket_id] = nums[i]
            
            # Remove bucket entry that's outside the window of indexDiff
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // w]
                
        return False

if __name__ == "__main__":
    print(Solution().containsNearbyAlmostDuplicate([1,2,5,6,7,2,4], 4, 0))  # True
    print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))    # False
    print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))        # True