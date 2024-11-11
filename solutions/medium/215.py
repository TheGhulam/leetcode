#Problem 215: Kth Largest Element in an Array

import random

def findKthLargest(nums, k):
    def quickSelect(left, right, k):
        if left >= right:
            return nums[left]
        
        # Randomly choose pivot and swap with right
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        pivot = nums[right]
        
        # Three-way partition
        lt = left      # elements < pivot
        i = left      # current element
        gt = right    # elements > pivot
        
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        
        if k <= gt and k >= lt:
            return pivot
        elif k < lt:
            return quickSelect(left, lt - 1, k)
        else:  # k > gt
            return quickSelect(gt + 1, right, k)
    
    k = len(nums) - k
    return quickSelect(0, len(nums) - 1, k)