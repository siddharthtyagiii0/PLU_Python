'''
Create a queue and insert the values 10, 20, 30, 40
'''
from collections import deque
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print("Queue =", queue)