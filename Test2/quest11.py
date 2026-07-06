
'''
Display the front element of the queue without removing 
'''
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print(queue[0])
print("Queue =", queue)