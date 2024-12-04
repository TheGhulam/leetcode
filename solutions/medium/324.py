#Problem 324: Wiggle Sort II

from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #Median using quickselect
        n = len(nums)
        median = self.findKLargest(nums, (n+1)//2)

        #3-way partition
        def idx(i):
            return (1+2*i) % (n|1)

        l, r, i = 0, n-1, 0

        while i <= r:
            if nums[idx(i)] > median:
                nums[idx(i)], nums[idx(l)] = nums[idx(l)], nums[idx(i)]
                l += 1
                i += 1
            elif nums[idx(i)] < median:
                nums[idx(i)], nums[idx(r)] = nums[idx(r)], nums[idx(i)]
                r -= 1
            else:
                i += 1
    
    def findKLargest(self, nums, k):
        def partition(l, r):
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        l, r = 0, len(nums)-1
        while l <= r:
            p = partition(l, r)
            if p == k-1:
                return nums[p]
            elif p < k-1:
                l = p+1
            else:
                r = p-1

        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 1, 1, 6, 4]
    s.wiggleSort(nums)
    print(nums)
    nums = [1, 3, 2, 2, 3, 1]
    s.wiggleSort(nums)
    print(nums)