#Problem 517: Super Washing Machines

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s, n = sum(machines), len(machines)
        if s % n != 0: return -1

        target = s // n
        max_moves = 0
        running_diff = 0

        for d in machines:
            diff = d - target
            running_diff += diff

            # Take max of
            # abs(running_diff): total dresses that need to pass through this point
            # diff: dresses that need to move from/to this single machine
            max_moves = max(max_moves, abs(running_diff), diff)

        return max_moves