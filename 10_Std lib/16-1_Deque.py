from collections import deque

d = deque(["task1", "task2", "task3"])

d.append("task4")

print(d)

print("Handling", d.popleft())

print(d)
