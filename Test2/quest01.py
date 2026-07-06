'''
Create a linked list containing the values 10, 20, 30, 40, 50 and display
all the elements.
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

current = head
while current:
    print(current.data, end=" ")
    current = current.next