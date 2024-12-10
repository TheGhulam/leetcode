#Problem 502: IPO

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()

        n = len(projects)
        curr_capital = w
        available_projects = [] # max heap of projects
        p_idx = 0

        for _ in range(k):
            while p_idx < n and projects[p_idx][0] <= curr_capital:
                heapq.heappush(available_projects, -projects[p_idx][1])
                p_idx += 1

            if not available_projects: break

            curr_capital += -heapq.heappop(available_projects)


        return curr_capital