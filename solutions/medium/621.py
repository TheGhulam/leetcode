#Problem 621: Task Scheduler

from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)

        max_freq = max(task_counts.values())
        max_count = sum(1 for task, count in task_counts.items() if count == max_freq)
        min_intervals = max((max_freq - 1) * (n + 1) + max_count, len(tasks))

        return min_intervals