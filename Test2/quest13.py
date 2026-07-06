'''Create the following binary tree:
```
50
/ \
30 70
```
Display the root, left child, and right child
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(50)
root.left = Node(30)
root.right = Node(70)
print("Root Node =", root.data)
print("Left Child =", root.left.data)
print("Right Child =", root.right.data)