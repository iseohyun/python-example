### list를 queue(큐)로 사용하기 ###


from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
print(queue)  # deque(['Eric', 'John', 'Michael', 'Terry'])

queue.append("Graham")  # Graham arrives
print(queue)  # deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

print(queue.popleft())  # "Eric" - The first to arrive now leaves
print(queue.popleft())  # "John" - The second to arrive now leaves

print(queue)  # deque(['Michael', 'Terry', 'Graham'])
