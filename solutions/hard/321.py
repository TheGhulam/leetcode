#Problem 321: Create Maximum Number

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)

        def maxArray(nums, t):
            stack = []
            to_pop = len(nums)-t

            for n in nums:
                while stack and stack[-1] < n and to_pop > 0:
                    stack.pop()
                    to_pop -= 1
                stack.append(n)
            
            return stack[:t]
        
        def merge(arr1, arr2):
            res = []
            while arr1 or arr2:
                if arr1 > arr2:
                    res.append(arr1[0])
                    arr1 = arr1[1:]
                else:
                    res.append(arr2[0])
                    arr2 = arr2[1:]
            return res

        max_num = []
        for i in range(max(0, k-n), min(k+1, m+1)):
            j = k - i
            candidate = merge(maxArray(nums1, i), maxArray(nums2, j))
            max_num = max(max_num, candidate)

        return max_num