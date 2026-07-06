'''
.Perform an Inorder Traversal on a binary tree.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)

def inorder(current):
    if current:
        inorder(current.left)
        print(current.data, end=" ")
        inorder(current.right)

inorder(root)