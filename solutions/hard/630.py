#Problem 630: Course Schedule III

from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])

        total_time = 0
        taken = []

        for duration, lastDay in courses:
            # Check if we can take this course
            if total_time + duration <= lastDay:
                # If we can finish before deadline, take it
                total_time += duration
                heappush(taken, -duration)  # negative for max heap
            elif taken and -taken[0] > duration:
                # If current course is shorter than our longest course
                # and switching would help us meet the deadline
                longest = -heappop(taken)
                total_time = total_time - longest + duration
                heappush(taken, -duration)
        
        return len(taken)