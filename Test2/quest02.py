'''
insert a new node containing 25 after the node containing 20
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

new_node = Node(25)

current = head

while current:
    if current.data == 20:
        new_node.next = current.next
        current.next = new_node
        current = None
    else:
        current = current.next

current = head

while current:
    print(current.data, end=" ")
    current = current.next