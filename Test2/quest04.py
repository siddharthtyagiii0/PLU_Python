
'''
Count and display the total number of nodes in the linked lis
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

count = 0
current = head

while current:
    count += 1
    current = current.next

print("Total Nodes =", count)