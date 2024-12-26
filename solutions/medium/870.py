#Problem 870: Advantage Shuffle

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        indexed_nums2 = [(n, i) for i, n in enumerate(nums2)]
        indexed_nums2.sort()

        res = [0] * n
        l = 0 # Smallest unused in nums1
        r = n-1 # Largest unused in nums1

        for i in range(n-1, -1, -1):
            num, idx = indexed_nums2[i]
            if nums1[r] > num:
                res[idx] = nums1[r]
                r -= 1
            else:
                res[idx] = nums1[l]
                l += 1
        
        return res