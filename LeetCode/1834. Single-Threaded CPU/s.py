"""
time: O(NlogN)
space: O(N)
todo: clean this up!
"""
from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [tuple(reversed(pair)) for pair in enumerate(tasks)]
        tasks.sort(key=lambda task: task[0])
        ENQUE_TIME, PROCESSING_TIME = 0, 1
        order = []
        heap = []
        current_time = 0
        i = 0

        def load_heap():
            nonlocal i
            while i < len(tasks) and (task := tasks[i])[0][ENQUE_TIME] <= current_time:
                heapq.heappush(heap, (task[0][PROCESSING_TIME], task[1]))
                i += 1

        def process_next_task():
            processing_time, index = heapq.heappop(heap)
            order.append(index)
            nonlocal current_time
            current_time += processing_time

        while i < len(tasks) or heap:
            load_heap()
            if heap:
                process_next_task()
            elif i < len(tasks):
                current_time = tasks[i][0][ENQUE_TIME]
        return order

print(Solution().getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
print(f"expected: [6,1,2,9,4,10,0,11,5,13,3,8,12,7]")