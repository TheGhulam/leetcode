#Problem 781: Rabbits in Forest

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)

        res = 0
        for a, freq in counts.items():
            group_size = a + 1
            num_groups = (freq + group_size - 1) // group_size
            res += num_groups * group_size
            
        return res