#! /usr/bin/env python

from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        max_so_far = 0
        chunks = 0
        
        for i in range(n):
            max_so_far = max(max_so_far, arr[i])
            
            # If the maximum equals the current position,
            # we can make a valid chunk
            if max_so_far == i:
                chunks += 1
                
        return chunks

if __name__ == "__main__":
    s = Solution()
    print(s.maxChunksToSorted([4,3,2,1,0]))
    print(s.maxChunksToSorted([1,0,2,3,4]))


