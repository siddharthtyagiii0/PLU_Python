'''
Display all the elements of the queue in FIFO order
'''
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print("elements in fifo order:")
for element in queue:
    print(element)