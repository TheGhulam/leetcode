#Problem 134: Gas Station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        curr_g = 0
        start = 0

        for i in range(len(gas)):
            curr_g += gas[i] - cost[i]
            if curr_g < 0:
                start = i + 1
                curr_g = 0

        return start