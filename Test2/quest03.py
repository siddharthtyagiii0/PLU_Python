'''
Delete the node containing 30 from the linked list and display the updated
list.
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
    if current.next and current.next.data == 30:
        current.next = current.next.next
        current = None
    else:
        current = current.next
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")