#Problem 1122: Relative Sort Array

from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        for i in arr1:
            freq[i] = freq.get(i, 0) + 1

        output = []
        for i in arr2:
            output.extend([i] * freq[i])
            del freq[i]

        for i in sorted(freq.keys()):
            output.extend([i] * freq[i])

        return output

if __name__ == "__main__":
    solution = Solution()

    # Expected: [2,2,2,1,4,3,3,9,6,7,19]
    print(solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))

    # Expected: [2,3,1,4,5]
    print(solution.relativeSortArray([1,2,3,4,5], [2,3,1,4]))

    # Expected: [1,2,3,4,5]
    print(solution.relativeSortArray([1,2,3,4,5], []))