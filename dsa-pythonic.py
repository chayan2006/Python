# 🧩 Data Structures and Algorithms (Pythonic Style)

from collections import deque
import heapq

# 1. Double-Ended Queue (deque) - Best for Stacks and Queues
# Much faster than lists for adding/removing from the START
dq = deque(["Task 1", "Task 2"])
dq.append("Task 3") # Add to right (O(1))
dq.appendleft("Urgent Task") # Add to left (O(1))
print("Deque Result:", dq)
dq.pop() # Remove from right
dq.popleft() # Remove from left (Fast!)

# 2. Priority Queue (Heaps) - Best for finding MIN/MAX instantly
# A binary tree where the smallest element is ALWAYS at the root
nums = [10, 2, 8, 5, 1, 9]
heapq.heapify(nums) # Convert list to min-heap in place
print("Smallest element is always at index 0:", nums[0]) 

# Pop smallest element
print("Popped smallest:", heapq.heappop(nums))
# Push new element
heapq.heappush(nums, 0)
print("Heap after push/pop:", nums)

# 3. Bisect (Binary Search on sorted lists)
import bisect
arr = [1, 3, 4, 4, 4, 6, 7]
# Find where 5 should be inserted to keep list sorted
pos = bisect.bisect_right(arr, 5) 
print("Insert 5 at position:", pos)

# 4. Built-in Linked List?
# Python doesn't have a linked-list class, but 'deque' behaves like one!
# For advanced trees/graphs, you usually build custom classes:
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Summary Table
"""
| DS / Tool | Best Used For                          | Performance (Worst Case) |
|-----------|----------------------------------------|---------------------------|
| List      | Simple arrays, random access           | O(n) (Insert at index 0) |
| Deque     | Queues (FIFO) or Stacks (LIFO)         | O(1) (Insert at ends)    |
| Heapq     | Priority Queues (Min/Max finding)     | O(log n) (Push/Pop)      |
| Bisect    | Binary search on SORTED data           | O(log n)                  |
| Dict      | Fast lookups by key (Hash Map)         | O(1) (Average)           |
"""
