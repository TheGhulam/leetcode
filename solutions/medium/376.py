#Problem 376: Wiggle Subsequence

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n

        length = 1 #First num always part of sequence
        prev_diff = None

        for i in range(1, n):
            curr_diff = nums[i] - nums[i-1]

            if (curr_diff != 0 and
            (prev_diff == None or
            (curr_diff > 0 and prev_diff < 0) or
            (curr_diff < 0 and prev_diff > 0))):
                length += 1
                prev_diff = curr_diff
        
        return length