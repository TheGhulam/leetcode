#Problem 826: Most Profit Assigning Work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()

        i = 0  # Index for jobs
        max_profit = 0 
        total_profit = 0 
        n = len(jobs)
        
        for ability in worker:
            while i < n and jobs[i][0] <= ability:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            
            total_profit += max_profit
        
        return total_profit