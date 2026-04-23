"""
https://leetcode.com/problems/design-task-manager/description/
"""
import heapq

class TaskManager(object):
    def __init__(self, tasks):
        self.heap = []
        self.taskPriority = {}
        self.taskOwner = {}
        for t in tasks:
            self.add(t[0], t[1], t[2])

    def add(self, userId, taskId, priority):
        heapq.heappush(self.heap, (-priority, -taskId))
        self.taskPriority[taskId] = priority
        self.taskOwner[taskId] = userId

    def edit(self, taskId, newPriority):
        heapq.heappush(self.heap, (-newPriority, -taskId))
        self.taskPriority[taskId] = newPriority

    def rmv(self, taskId):
        self.taskPriority[taskId] = -1

    def execTop(self):
        while self.heap:
            negp, negid = heapq.heappop(self.heap)
            p = -negp
            tid = -negid
            if self.taskPriority.get(tid, -2) == p:
                self.taskPriority[tid] = -1
                return self.taskOwner.get(tid, -1)
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

# Unit tests
import unittest

class TestTaskManager(unittest.TestCase):

    def test_case_1(self):
        tasks = [[1, 101, 5], [2, 102, 3], [3, 103, 4]]
        manager = TaskManager(tasks)
        self.assertEqual(manager.execTop(), 1)  # Task 101 with priority 5
        manager.add(4, 104, 6)
        self.assertEqual(manager.execTop(), 4)  # Task 104 with priority 6
        manager.edit(102, 7)
        self.assertEqual(manager.execTop(), 2)  # Task 102 with updated priority 7
        manager.rmv(103)
        self.assertEqual(manager.execTop(), -1) # No tasks left

    def test_case_2(self):
        tasks = [[1, 201, 1], [2, 202, 2]]
        manager = TaskManager(tasks)
        manager.rmv(201)
        self.assertEqual(manager.execTop(), 2)  # Task 202 with priority 2
        self.assertEqual(manager.execTop(), -1) # No tasks left

if __name__ == "__main__":
    unittest.main()