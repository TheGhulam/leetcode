#Problem 3242: Shortest Distance After Road Addition Queries I

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(n-1):
            graph[i].append(i + 1)
        o = []

        for u, v in queries:
            graph[u].append(v)
            
            # Find shortest path using BFS
            dist = [-1] * n
            dist[0] = 0
            queue = deque([0])
            
            while queue and dist[n-1] == -1:
                curr = queue.popleft()
                for next_city in graph[curr]:
                    if dist[next_city] == -1:
                        dist[next_city] = dist[curr] + 1
                        queue.append(next_city)
            
            # If no path exists, use n (or some large number)
            o.append(dist[n-1] if dist[n-1] != -1 else n)

        return o