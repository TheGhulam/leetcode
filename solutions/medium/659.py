#Problem 659: Split Array into Consecutive Subsequences

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        print(counts)

        # end[i] = number of sequences ending at number i
        end = {} # keeps track of how many sequences are waiting for each number

        for n in nums:
            if counts[n] == 0:
                continue
            
            # Try adding in existing sequence
            if n in end and end[n] > 0:
                end[n] -= 1
                end[n+1] = end.get(n+1, 0) + 1
            # Try starting a new sequence
            elif counts.get(n+1, 0) > 0 and counts.get(n+2, 0) > 0:
                counts[n+1] -= 1
                counts[n+2] -= 1
                end[n+3] = end.get(n+3, 0) + 1
            else:
                return False
            
            counts[n] -= 1
        
        return True